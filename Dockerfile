### Derive from the base container image
FROM doduo1.umcn.nl/uokbaseimage/diag:tf2.12-pt2.0-v1

# Clone GitHub repo
RUN git clone -b feature/add-inference-run https://github.com/DIAGNijmegen/DuneAI-Automated-detection-and-segmentation-of-non-small-cell-lung-cancer-computed-tomography-images.git /root/dune-ai

# Change directory to the repo if needed
WORKDIR /root/dune-ai

# Verify the requirements.txt file is present
RUN ls -l requirements.txt

### Install python packages
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt