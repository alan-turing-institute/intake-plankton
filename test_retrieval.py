import intake

catlg = intake.open_catalog('plktn.yaml')

dk = catlg['foo'].to_dask()