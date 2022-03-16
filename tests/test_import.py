import pytest

def test_workflow():
    from scivision.io import load_pretrained_model, load_dataset

    scivision_yml = 'https://raw.githubusercontent.com/alan-turing-institute/mapreader-plant-scivision/main/.scivision-config.yaml'
    
    model = load_pretrained_model(scivision_yml, allow_install=True)

    cat = load_dataset('https://github.com/alan-turing-institute/mapreader-plant-scivision')

    # --- plant_single dataset
    ds = cat.plant_single().to_dask()

    outputs = model.predict(ds[0], plot_output=False)
    assert len(outputs) == 30
    
    outputs = model.predict(ds[1], plot_output=False)
    assert len(outputs) == 30
    
    # --- plant_flower dataset 
    ds = cat.plant_flower().to_dask()

    outputs = model.predict(ds[0], plot_output=False)
    
    outputs = model.predict(ds[1], plot_output=False)
