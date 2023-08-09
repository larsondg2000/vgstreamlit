import torch
from typing import List
from torchvision import transforms
from PIL import Image
import matplotlib.pyplot as plt
from pathlib import Path
import streamlit as st


def load_checkpoint(model_checkpoint):
    """ Loads saved model checkpoint """
    saved_model = torch.load(model_checkpoint)
    model = saved_model['arch']

    return model


def predict_image(model, custom_image_path, class_names, gpu):
    """ predicts an individual image """
    pred_and_plot_image(model=model,
                        image_path=custom_image_path,
                        class_names=class_names,
                        transform=None,
                        gpu=gpu)


def pred_and_plot_image(model, image_path, class_names, transform, gpu):
    """
    Predicts on a target image with a target model.

    Args:
        model (torch.nn.Module): A trained (or untrained) PyTorch model to predict on an image.
        class_names (List[str]): A list of target classes to map predictions to.
        image_path (str): Filepath to target image to predict on.
        transform (torchvision.transforms, optional): Transform to perform on image.
        Defaults to None which uses ImageNet normalization.
        gpu: cuda or cpu
   """

    # Open image- convert('RGB') fixes issue with png images
    img = Image.open(image_path).convert('RGB')

    # Create transforms from image (if one doesn't exist)
    if transform is not None:
        image_transform = transform
    else:
        image_transform = transforms.Compose(
            [
                transforms.Resize(size=256),
                transforms.CenterCrop(size=224),
                transforms.ToTensor(),
                transforms.Normalize(
                    mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]
                ),
            ]
        )


    # Make sure the model is on the target device
    cuda = torch.cuda.is_available()

    if gpu and cuda:
        model.cuda()
    else:
        model.cpu()

    # Turn on model evaluation mode and inference mode
    model.eval()
    with torch.inference_mode():
        # Transform and add an extra dimension to image
        # (model requires samples in [batch_size, color_channels, height, width])
        transformed_image = image_transform(img).unsqueeze(dim=0)

        # Move input and label tensors to the (default device= cpu)
        if gpu and cuda:
            transformed_image = transformed_image.cuda()

        else:
            transformed_image = transformed_image.cpu()

        # Make a prediction on image with an extra dimension and send it to the target device
        target_image_pred = model(transformed_image)

    # Convert logits -> prediction probabilities (using torch.softmax() for multi-class classification)
    target_image_pred_probs = torch.softmax(target_image_pred, dim=1)

    # Convert prediction probabilities -> prediction labels
    target_image_pred_label = torch.argmax(target_image_pred_probs, dim=1)

    # Get model name
    model_name = model.__class__.__name__

    # image_is = check_prediction(image_path, target_image_pred_label, class_names)

    # Plot image with predicted label and probability

    st.markdown("<h5 style='color: red;'>"
                f"Pred: {class_names[target_image_pred_label]} | Prob: {target_image_pred_probs.max() * 100:.1f}% | Model: {model_name}"
                "</h5>", unsafe_allow_html=True)
    st.image(img, width=400)


