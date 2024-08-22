"""line with dataframe:"""
import pandas as pd
import matplotlib.pyplot as plt

# dataframe
data = pd.DataFrame(
    {
        "cricket_Bat":["HRS","SG","TON","GM"],
        "MRP":[1232,3452,5234,9843],
        "Weight_Gram":[1100,980,1000,750]
}
)

# create data frame
dataframe = pd.DataFrame(data)

# plot line using pyplot sub module
plt.plot(dataframe["cricket_Bat"],dataframe["MRP"],dataframe["Weight_Gram"])
plt.show()