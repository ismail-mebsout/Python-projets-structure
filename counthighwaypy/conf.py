import os

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.realpath(__file__), "../.."))

##### directories
DATA_DIR = os.path.join(PROJECT_ROOT, "data/")
NOTEBOOK_DIR = os.path.join(PROJECT_ROOT, "notebooks")

SRC_DIR = os.path.join(PROJECT_ROOT, "counthighwaypy/")
WEIGHTS_DIR = os.path.join(PROJECT_ROOT, "weights/")

MODULE_DETECT_VEHICLE_DIR = os.path.join(SRC_DIR, "detectvehicle/")
MODULE_DETECT_LICENCE_PLATE_DIR = os.path.join(SRC_DIR, "detectlicenseplate/")
MODULE_OCR_LICENSE_PLATE_DIR = os.path.join(SRC_DIR, "ocrlicenseplate/")

