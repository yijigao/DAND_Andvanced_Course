Citation Request:
  This dataset is public available for research. The details are described in [Cortez et al., 2009]. 
  Please include this citation if you plan to use this database:

  P. Cortez, A. Cerdeira, F. Almeida, T. Matos and J. Reis. 
  Modeling wine preferences by data mining from physicochemical properties.
  In Decision Support Systems, Elsevier, 47(4):547-553. ISSN: 0167-9236.

  Available at: [@Elsevier] http://dx.doi.org/10.1016/j.dss.2009.05.016
                [Pre-press (pdf)] http://www3.dsi.uminho.pt/pcortez/winequality09.pdf
                [bib] http://www3.dsi.uminho.pt/pcortez/dss09.bib

1. Title: Wine Quality 

2. Sources
   Created by: Paulo Cortez (Univ. Minho), Antonio Cerdeira, Fernando Almeida, Telmo Matos and Jose Reis (CVRVV) @ 2009
   
3. Past Usage:

  P. Cortez, A. Cerdeira, F. Almeida, T. Matos and J. Reis. 
  Modeling wine preferences by data mining from physicochemical properties.
  In Decision Support Systems, Elsevier, 47(4):547-553. ISSN: 0167-9236.

  In the above reference, two datasets were created, using red and white wine samples.
  The inputs include objective tests (e.g. PH values) and the output is based on sensory data
  (median of at least 3 evaluations made by wine experts). Each expert graded the wine quality 
  between 0 (very bad) and 10 (very excellent). Several data mining methods were applied to model
  these datasets under a regression approach. The support vector machine model achieved the
  best results. Several metrics were computed: MAD, confusion matrix for a fixed error tolerance (T),
  etc. Also, we plot the relative importances of the input variables (as measured by a sensitivity
  analysis procedure).
 
4. Relevant Information:

   The two datasets are related to red and white variants of the Portuguese "Vinho Verde" wine.
   For more details, consult: http://www.vinhoverde.pt/en/ or the reference [Cortez et al., 2009].
   Due to privacy and logistic issues, only physicochemical (inputs) and sensory (the output) variables 
   are available (e.g. there is no data about grape types, wine brand, wine selling price, etc.).

   These datasets can be viewed as classification or regression tasks.
   The classes are ordered and not balanced (e.g. there are munch more normal wines than
   excellent or poor ones). Outlier detection algorithms could be used to detect the few excellent
   or poor wines. Also, we are not sure if all input variables are relevant. So
   it could be interesting to test feature selection methods. 

5. Number of Instances: red wine - 1599; white wine - 4898. 

6. Number of Attributes: 11 + output attribute
  
   Note: several of the attributes may be correlated, thus it makes sense to apply some sort of
   feature selection.

7. Attribute information:

   For more information, read [Cortez et al., 2009].

   Input variables (based on physicochemical tests):
   1 - fixed acidity (tartaric acid - g / dm^3)
   2 - volatile acidity (acetic acid - g / dm^3)
   3 - citric acid (g / dm^3)
   4 - residual sugar (g / dm^3)
   5 - chlorides (sodium chloride - g / dm^3
   6 - free sulfur dioxide (mg / dm^3)
   7 - total sulfur dioxide (mg / dm^3)
   8 - density (g / cm^3)
   9 - pH
   10 - sulphates (potassium sulphate - g / dm3)
   11 - alcohol (% by volume)
   Output variable (based on sensory data): 
   12 - quality (score between 0 and 10)
***

    1 - 固定酸度（酒石酸 - g / dm ^ 3）
    2 - 挥发酸度（乙酸 - g / dm ^ 3）
    3 - 柠檬酸（g / dm ^ 3）
    4 - 残糖（g / dm ^ 3）
    5 - 氯化物（氯化钠 - g / dm ^ 3
    6 - 游离二氧化硫（mg / dm ^ 3）
    7 - 总二氧化硫（mg / dm ^ 3）
    8 - 密度（g / cm ^ 3）
    9 - pH
    10 - 硫酸盐（硫酸钾 - g / dm3）
    11 - 酒精（体积百分比）
    输出变量（基于感官数据）：
    12 - 品质（0到10分）
***

8. Missing Attribute Values: None

9. Description of attributes:
   
 ***
 
    1 - 固定酸度：葡萄酒中涉及的大多数酸或固定或非挥发性（不易挥发）

    2 - 挥发性酸度：葡萄酒中醋酸的含量过高会导致醋的味道不舒服

    3 - 柠檬酸：少量发现，柠檬酸可以增加“新鲜”和风味的葡萄酒
    4 - 残糖：发酵停止后剩余的糖的量，很少发现低于1克/升的葡萄酒，高于45克/升的葡萄酒被 为是甜的

    5 - 氯化物：酒中的盐量

    6 - 游离二氧化硫：SO2的游离形式存在于分子SO2（作为溶解气体）和亚硫酸氢根离子的平衡状态;它可以防止微生物的生长和葡萄酒的氧化

    7 - 总二氧化硫：游离和结合形式的SO2的量;在低浓度下，SO2在葡萄酒中几乎检测不到，但是当游离SO2浓度超过50ppm时，SO2在葡萄酒的鼻子和味道中变得明显

    8 - 密度：取决于酒精和糖的百分比，水的密度接近于水的密度

    9 - 酸碱度：描述葡萄酒的酸度或碱度是从0（非常酸性）到14（非常碱性）的等级。大多数葡萄酒的pH值在3-4之间

    10 - 硫酸盐：一种能够促成二氧化硫气体（SO2）水平的葡萄酒添加剂，它起抗菌剂和抗氧化剂的作用

    11 - 酒精：酒的百分比酒精含量

    输出变量（基于感官数据）：
    12 - 质量（分数在0和10之间）

***
   