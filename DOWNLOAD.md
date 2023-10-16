Dataset **PCBSegClassNet** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/h/s/um/2nyl7WFB0SSycGepavUD3pKCoKv3qNtWeQlotlljCMwtRAVRTYGislCEQX9iNiby26KowsF6mEDd4AaXAXeJpfups8pT5rymqPxvAEr4uXtIa4B23hMPT0o49BPZ.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='PCBSegClassNet', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be [downloaded here](https://www.kaggle.com/datasets/aditidankar/pcbsegclassnet/download?datasetVersionNumber=1).