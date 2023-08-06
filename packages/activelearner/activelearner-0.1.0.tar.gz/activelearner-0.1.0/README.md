# Active Learner

A Python package which will do Active Learning process to determine whether to use Text Classification or Topic Modeling. For Usage of this package, you need to consist of a dataset which has folders to represent the classes for Text Classification, and contain text files in each class folders.

## Usage

### Example

Following query will allow to find thresholds for the classes available in the dataset. In which `directory` is the directory of your dataset, and `file` is the name of the file needed to find similarity.

```
from activelearner import similarity
from activelearner import threshold

threshold = threshold(directory)
similarity = similarity(file, directory,threshold)
```
