from Automatic_segmentation_script.TheDuneAI import (ContourPilot as cp)
import argparse


def run_inference(input_folder: str, output_folder: str, model_folder: str):
    """
    Run inference on selected scans and save the results in the output folder.
    Args:
        input_folder: path to the folder containing the scans to run inference on
        output_folder: path to the output folder
        model_folder: path to the folder containing the model weights
    """

    # Initialize the model
    model = cp(model_path=model_folder, data_path=input_folder, output_path=output_folder, verbosity=True)
    # Inference
    model.segment()


if __name__ == '__main__':

    parser = argparse.ArgumentParser(prog='Inference Primakov')
    parser.add_argument("--input", type=str, help="Path to the folder containing scans for inference.")
    parser.add_argument("--output", type=str, help="Path to the output folder containing inference results.")
    parser.add_argument("--model", type=str, help="Path to the folder containing the model weights to be used for "
                                                  "inference.")

    option = parser.parse_args()
    input = option.input
    output = option.output
    model = option.model
    # Run inference
    run_inference(input_folder=input, output_folder=output, model_folder=model)