reddit <- read.csv("reddit.csv")

reddit

library(ggplot2)
qplot(data = reddit, x = age.range)
qplot(data = reddit, x = income.range)

# Setting Level of Ordered Factor Solution 
reddit$age.range <- ordered(reddit$age.range, levels = c("Under 18", "18-24","25-34","35-44","45-54",
                                                         "55-64","65 of Above"))
qplot(data = reddit, x = age.range)

# Alternate Solution 
reddit$age.range <- factor(reddit$age.range, levels = c("Under 18", "18-24","25-34","35-44","45-54",
                                                        "55-64","65 of Above"), ordered = T)
qplot(data = reddit, x = age.range)
?factor

# factor function 
