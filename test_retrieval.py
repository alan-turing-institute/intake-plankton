import intake

catlg = intake.open_catalog('plktn.yaml')

source = 'single_img'

img = catlg[source].to_dask()