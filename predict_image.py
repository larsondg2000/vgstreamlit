from predict_functions import load_checkpoint, predict_image


def main():
    """
    checks individual image prediction

    :return:
    """
    gpu = "gpu"
    model = load_checkpoint("RegNet_checkpoint.pth")
    class_names = ['not_vangogh', 'vangogh']
    custom_image_path = "images/stone_quarry_quest.jpg"
    predict_image(model, custom_image_path, class_names, gpu)


if __name__ == "__main__":
    main()
