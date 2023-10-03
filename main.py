from pyexcel_ods3 import save_data 
from collections import OrderedDict
 
data = OrderedDict()
data.update({"Sheet 1": [[],[],[1, 2, 3], [4, 5, 6]]})
save_data("test.ods", data)