library(jiebaR)
library(wordcloud2)
library(dplyr)
rm(list=ls(all=TRUE))

my_colors <- c( "#140a02","#5d5d5d",
                        "#73543e", "#bda67e",  "#8E99A3", "#B4A592", "#bda67e",  "#5d5d5d", "#73543e","gold")
                                          
myword=scan(file="ObjectName.txt",what="",encoding="ANSI")

myworker<-worker(type='mix')

result=segment(myword,myworker)
result <- result[nchar(result)>1]
result=sort(table(result),decresing=T)
result <- rev(result)
write.csv(result,'result_re.csv')


wordcloud2(result[1:50], size = 1.3, color = my_colors, backgroundColor = "transparent", fontFamily = "Big Caslon")
