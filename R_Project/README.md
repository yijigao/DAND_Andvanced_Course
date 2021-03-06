---
output: html_document
editor_options: 
  chunk_output_type: inline
---
WineQualityWhites by yijigao92@gmail.com
========================================================
```{r global_options, include=FALSE}
knitr::opts_chunk$set(message = FALSE, warning = FALSE, echo = FALSE)
```




```{r echo=FALSE, message=FALSE, warning=FALSE, packages}
# Load all of the packages that you end up using
# in your analysis in this code chunk.

# Notice that the parameter "echo" was set to FALSE for this code chunk.
# This prevents the code from displaying in the knitted HTML output.
# You should set echo=FALSE for all code chunks in your file.

library(ggplot2)
library(gridExtra)
library(GGally)
library(scales)
library(memisc)
library(ggthemes)

theme_set(theme_few())
```

```{r echo=FALSE, Load_the_Data}
# Load the Data
WineQualityWhites <- read.csv("wineQualityWhites.csv")

```

# Univariate Plots Section
```{r echo=FALSE, Univariate_Plots}
dim(WineQualityWhites)
str(WineQualityWhites)
summary(WineQualityWhites)
```

数据集中包含了13个变量，4898个观察值

```{r echo=FALSE}
table(WineQualityWhites$quality)

ggplot(WineQualityWhites, aes(quality)) +
  geom_histogram(binwidth = 1,fill = "#0000 CD") +
  ggtitle("Quality")

```

数据集中的品质大致呈正态分布，大多数的白葡萄酒品质在5-7之间。品质很高和很低的酒数量都不多。

```{r echo=FALSE}
table(WineQualityWhites$fixed.acidity)
ggplot(WineQualityWhites, aes(fixed.acidity)) +
  geom_histogram(binwidth = 0.1,fill = "#0000CD") +
  ggtitle("Fix acidity")
```

白葡萄酒的固定酸度在6-8之间，呈正态分布；

```{r echo=FALSE, message=FALSE, warning=FALSE}

f1 <-  ggplot(WineQualityWhites, aes(volatile.acidity)) +
  geom_histogram(fill = "#0000CD")

f2 <- ggplot(WineQualityWhites, aes(volatile.acidity), xlab) +
  geom_histogram(fill = "#8A2BE2")+
  xlab("volatile.acidity(log10)")
  scale_x_log10()

f3 <- ggplot(WineQualityWhites, aes(residual.sugar)) +
  geom_histogram(fill = "#0000CD")

f4 <- ggplot(WineQualityWhites, aes(residual.sugar)) +
  geom_histogram(fill = "#8A2BE2") +
  scale_x_log10() +
  xlab("residual.sugar(log10)")

f5 <- ggplot(WineQualityWhites, aes(chlorides)) +
  geom_histogram(fill = "#0000CD")

f6 <- ggplot(WineQualityWhites, aes(chlorides)) +
  geom_histogram(fill = "#8A2BE2") +
  scale_x_log10() +
  xlab("chlorides(log10)")

f7 <- ggplot(WineQualityWhites, aes(free.sulfur.dioxide)) +
  geom_histogram(fill = "#0000CD")

f8 <- ggplot(WineQualityWhites, aes(free.sulfur.dioxide)) +
  geom_histogram(fill = "#8A2BE2") +
  scale_x_log10() +
  xlab("free.sulfur.dioxide(log10)")

grid.arrange(f1, f2, f3, f4, f5, f6, f7, f8, ncol = 2)
```

白葡萄酒的挥发性酸度/残糖/氯化物/游离二氧化硫，呈现正的偏斜，有长的尾值，将其转换为对数后呈明显的正态分布，有趣的是，残糖出现两个最大值。


```{r echo=FALSE, message=FALSE}

ggplot(WineQualityWhites, aes(total.sulfur.dioxide)) +
  geom_histogram(fill = "#0000CD") +
  ggtitle("Total sulfur dioxide")

ggplot(WineQualityWhites, aes(density)) +
  geom_histogram(fill = "#0000CD") +
  ggtitle("Density")

ggplot(WineQualityWhites, aes(pH)) +
  geom_histogram(fill = "#0000CD") +
  ggtitle("pH")

ggplot(WineQualityWhites, aes(sulphates)) +
  geom_histogram(fill = "#0000CD") +
  ggtitle("Sulphates")

```

柠檬酸、总二氧化硫、密度、pH、硫酸盐均大致呈正态分布。

```{r echo=FALSE, message=FALSE, warning=FALSE}
ggplot(WineQualityWhites, aes(alcohol)) +
  geom_histogram(fill = I("#0000CD")) +
  ggtitle("Alcohol")

ggplot(WineQualityWhites, aes(alcohol)) +
  geom_histogram(fill = I("#0000CD")) +
  ggtitle("Alcohol") +
  scale_x_log10() +
  xlab("Alcohol(log10)")
```




# Univariate Analysis

### What is the structure of your dataset?
一共有13个变量，4898个观察值。

* 白葡萄酒品质平均值为5.88，75%的白葡萄酒品质在5以上
* 大多数白葡萄酒的固定酸度6-8之间
* 白葡萄酒的残糖含量为1-2之间的数量最多
* 白葡萄酒的pH范围为2.7-3.8，平均值为3.19

### What is/are the main feature(s) of interest in your dataset?
我最感兴趣的是白葡萄酒的品质，我想知道哪个变量对于预测白葡萄酒的品质最相关

### What other features in the dataset do you think will help support your investigation into your feature(s) of interest?
固定酸度，残糖，pH，酒精

### Did you create any new variables from existing variables in the dataset?
未创建新变量

### Of the features you investigated, were there any unusual distributions? Did you perform any operations on the data to tidy, adjust, or change the form of the data? If so, why did you do this?
挥发性酸度，残糖含量，氯化物，游离二氧化硫，我将这些数据取对数，使之分布趋于正态分布，便于分析。


# Bivariate Plots Section
```{r echo=FALSE, Bivariate_Plots}
cor(WineQualityWhites)
```

为了研究quality究竟与哪些变量相关，先概览下quality与各变量的相关系数，可以看到，quality与alcohol, density相关性最强，其次是volatile.acidity, chlorides, total.sulfur.dioxide, 与citric.acidity, residual.sugar, free.sulfur.dioxide, pH, sulphates相关性不大

```{r fig.width=15, fig.height=15}
ggpairs(WineQualityWhites, 
        lower = list(continuous = wrap("points", shape = I("."))),
        upper = list(combo = wrap("box", outlier.shape = I("."),
                                  continuous = wrap("cor", size = 3))))
```

```{r echo=FALSE, message=FALSE}
ggplot(WineQualityWhites, aes(factor(quality),alcohol)) +
  geom_point()

ggplot(WineQualityWhites, aes(factor(quality),alcohol)) +
  geom_point(alpha = 0.3, size =2, position = "jitter")
```

绘制了酒精-品质散点图，第一张图可以看出过度绘制，对图添加抖动，从酒精与品质的散点图可以看出，酒精浓度越高，高品质的酒更集中，大致呈正相关关系。

```{r message=FALSE, warning=FALSE, echo=FALSE}
ggplot(WineQualityWhites, aes(factor(quality),density)) +
  geom_point(alpha = 1/10, size = 2, position = "jitter") +
  ylim(min(WineQualityWhites$density), quantile(WineQualityWhites$density, .99))
```

从密度-品质散点图看，密度的白葡萄酒的品质在5集中更多，而低密度的酒高品质集中。这个结果也好理解，因为酒精浓度越高，密度越小，我们可以来看酒精浓度与酒密度的关系

```{r echo=FALSE, message=FALSE, warning=FALSE}
ggplot(WineQualityWhites, aes(alcohol, density)) +
  geom_point(alpha = 1/20,size = 1.5, position = "jitter") +
  geom_smooth(method = "lm") +
  ylim(min(WineQualityWhites$density), quantile(WineQualityWhites$density, .99))

```

上图证实了我们的解释，酒的密度随酒精浓度升高而降低。

```{r echo=FALSE, message=FALSE, warning=FALSE}
ggplot(WineQualityWhites, aes(factor(quality), volatile.acidity)) +
  geom_point(alpha = 0.3, size = 1.5, position = "jitter")

ggplot(WineQualityWhites,aes(factor(quality), chlorides))+
  geom_point(alpha = 0.3, size = 1.5, position = "jitter") +
  ylim(0, quantile(WineQualityWhites$chlorides, .99))
```

看起来volatile.acidity 和 chlorides 呈负相关

```{r echo=FALSE, message=FALSE}

by(WineQualityWhites$alcohol, factor(WineQualityWhites$quality), summary)

ggplot(WineQualityWhites, aes(x = factor(quality), y = alcohol)) +
   geom_jitter(alpha = 0.1) +
   geom_boxplot(alpha = 0.5, size = 0.5) +
   theme_gray()
```

```{r}
by(WineQualityWhites$density, factor(WineQualityWhites$quality), summary)

ggplot(WineQualityWhites, aes(x = factor(quality), y = density)) +
   geom_jitter(alpha = 0.1) +
   geom_boxplot(alpha = 0.5, size = 0.5) +
   coord_cartesian(ylim = c(0.989, 1.000)) +
   theme_gray()
```


为了进一步研究与品质相关的因素，我作图时使用factor将quality变量转化为ordered类型变量,上图是分别是quality与alcohol浓度, density的箱线图，可以明显看出，高品质的白葡萄酒alcohol中位数要高于低品质白葡萄酒,density中位数高品质酒明显低于低品质酒。

```{r echo=FALSE, message=FALSE}
by(WineQualityWhites$volatile.acidity, factor(WineQualityWhites$quality), summary)

ggplot(WineQualityWhites, aes(x = factor(quality), y = volatile.acidity)) +
   geom_jitter(alpha = 0.1) +
   geom_boxplot(alpha = 0.5, size = 0.5) +
   coord_cartesian(ylim = c(0, 0.55)) +
   theme_gray()

```


```{r echo=FALSE, message=FALSE}
by(WineQualityWhites$chlorides, factor(WineQualityWhites$quality), summary)
ggplot(WineQualityWhites, aes(x = factor(quality), y = chlorides)) +
  geom_jitter(alpha = 0.1) +
  geom_boxplot(alpha = 0.5, size = 0.5) +
  coord_cartesian(ylim = c(0, 0.101)) +
  theme_gray()
```


从上面的箱线图我们发现，不同品质得分的volatile.acidity相差不大，而对于chlorides, 明显的，高品质的白葡萄酒的chlorides要低于低品质的酒。

# Bivariate Analysis

### Talk about some of the relationships you observed in this part of the investigation. How did the feature(s) of interest vary with other features in the dataset?

在这一部分，我研究了与白葡萄酒quality相关系数较大的几个变量（alcohol, density, volatile.acidty, chlorides）。
结果如下：

* 白葡萄酒quality与alcohol正相关，alcohol浓度越大，quality得分越高；
* chlorides越低，quality得分越高。
* quality与volatile.acidity相关性不大。

### Did you observe any interesting relationships between the other features (not the main feature(s) of interest)?

density 与 alcohol 呈负相关，alcohol浓度越高，density越低，quality得分越高

### What was the strongest relationship you found?

quality 与alcohol浓度有较强相关


# Multivariate Plots Section

```{r echo=FALSE, warning=FALSE, Multivariate_Plots}

ggplot(WineQualityWhites, aes(x = alcohol, y = density, color = factor(quality))) +
  geom_jitter(alpha = 0.2) +
  ylim(0.985, 1.005) +
  scale_color_brewer(palette = 18) +
  geom_smooth(method = "lm", se = FALSE, size = 1) +
  labs(x = "Alcohol", y = "Density") +
  ggtitle("Density VS Alcohol VS Quality") +
  theme_gray()
```

上图是density-alcohol使用quality着色的多变量图， density与alcohol负相关，也能看到较高品质的酒分布于图的右下角，即alcohol较大，density较小的区域

```{r echo=FALSE, message=FALSE, warning=FALSE}
ggplot(WineQualityWhites, aes(residual.sugar, density, color = factor(quality))) +
  geom_jitter(alpha = 0.3) +
  xlim(0, quantile(WineQualityWhites$residual.sugar, .99)) +
  ylim(0.985, 1.005) +
  geom_smooth(method = "lm", se = FALSE, size = 1) +
  scale_color_brewer(palette = 18) +
  labs(x = "Residual Sugar", y = "Density") +
  ggtitle("Density VS Residual Sugar VS Quality")

```

residual.sugar 与 density 相关， 而density越低，quality越高

```{r echo=FALSE, message=FALSE, warning=FALSE}

ggplot(WineQualityWhites, aes(total.sulfur.dioxide, density, color = factor(quality))) +
  geom_jitter(alpha = 0.3) +
  geom_smooth(method = "lm", se = FALSE, size = 1) +
  ylim(0.985, 1.005) +
  scale_color_brewer(palette = 18) +
  labs(x = "Total sulfur dioxide", y = "Density") +
  ggtitle("Density VS Total sulfur dioxide VS Quality")
```


# Multivariate Analysis

### Talk about some of the relationships you observed in this part of the investigation. Were there features that strengthened each other in terms of looking at your feature(s) of interest?

这一部分进一步考察了qulaity与density、alcohol、residual.sugar、total.sulfur.dioxide间的关系，这部分也验证了quality与alcohol、density的强相关关系，而对于residual.sugar，total.sulfur.dioxide，虽然其与density相关性强，但是似乎对quality影响不大

### Were there any interesting or surprising interactions between features?

density与多个变量如alcohol，residual.sugal，total.sulfur.dioxide都有，线性相关，而alcohol影响最大

### OPTIONAL: Did you create any models with your dataset? Discuss the strengths and limitations of your model.

------

# Final Plots and Summary

### Plot One
```{r echo=FALSE, Plot_One}
ggplot(WineQualityWhites, aes(quality, fill = I("#4169E1"))) +
  geom_histogram(binwidth = 1) +
  ggtitle("Quality")
```

### Description One

白葡萄酒的quality得分呈正态分布，大部分得分在5-7之间

### Plot Two

```{r echo=FALSE, Plot_Two}
ggplot(WineQualityWhites, aes(factor(quality), alcohol)) +
  geom_boxplot(alpha = 0.5, size = 0.75) +
  geom_jitter(alpha = 0.1) +
  ggtitle("Quality vs alcohol") +
  labs(x = "Quality", y = "Alcohol") +
  theme_gray()


```

### Description Two

quality得分高的白葡萄酒的alcohol浓度都较高

### Plot Three

```{r echo=FALSE,message=FALSE,warning=FALSE,Plot_Three}
ggplot(WineQualityWhites, aes(x = alcohol, y = density, color = factor(quality))) +
  geom_jitter(alpha = 0.2) +
  ylim(0.985, 1.005) +
  scale_color_brewer(palette = 18) +
  geom_smooth(method = "lm", se = FALSE, size = 1) +
  labs(x = "Alcohol", y = "Density") +
  ggtitle("Density VS Alcohol VS Quality") +
  theme_gray()
```

### Description Three

上图揭示了alcohol与density 的线性关系，同时揭示了quality与alcohol的正相关及density的负相关关系。

------

# Reflection

这份数据集包含了白葡萄酒的13个变量，我主要想研究白葡萄酒quality与哪些变量最相关。以下是本次分析的反思和总结：

* 我在分析两个变量和多个变量时遇到了挫折，因为数据集中没有类别变量，解决方案是考虑到quality只有7种取值，我将它转化为类别变量。但是这为我后面建立预测模型也带来了麻烦，所以这部分处理不好。
* 我最终找到了与白葡萄酒quality最相关的变量，即alcohol，alcohol浓度越高，白葡萄酒品质越高。
* 将来的工作中，我还希望建立一个能够对葡萄酒品质进行预测的模型，通过其化学检测性质来预测其品质得分。
