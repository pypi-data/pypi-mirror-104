#Purpose: Combining P-values methodology
#Author: Breya McGlown
#Math Master's Thesis

#install.packages('metap')
#install.packages("metap", repo = "https://CRAN.R-project.org/package=metap ")
#install.packages("utils" , repo = "https://lib.ugent.be/CRAN/")
#BiocManager::install("EmpiricalBrownsMethod")
library(chi)
library(metap)
library(EmpiricalBrownsMethod)
require(utils)

myClass <- function(x){
    "Functions within this class allow for multiple p values
    to be defined within each method below
    Method options include: Fisher, Pearson, Ed, Stouffer, George, Tippett"

    self.method<- x
    structure(class = "myClass", list(
        #methods
        #FishersMethod
        InfinitePs = function(x,...){
            kwargs<-list(...)
            return(c(x,kwargs))     
            },
        FishersMethod = function(x) {
            if (self.method == "Fisher"){
            k <- 1
            Len<- length(x)
            temp <-vector("list",Len)
            for (i in x) {
            temp[[k]]<-log(i)
            k <- k + 1
            }
            temp1 <- Reduce("+",temp)
            output <- -2 * temp1
            return(output)
            }
        },
        #PearsonsMethod
        PearsonsMethod = function(x) {
            if (self.method == "Pearson"){
            k <- 1
            Len<- length(x)
            temp <-vector("list",Len)
            for (i in x) {
            temp[[k]]<- (-(log(1-i)))
            k <- k + 1
            }
            temp1 <- Reduce("+",temp)
            output <- -2 * temp1
            return(output)
            }
        },

        #GeorgeMethod
        GeorgeMethod = function(x) {
            if (self.method == "George"){
            k <- 1
            Len<- length(x)
            temp <-vector("list",Len)
            for (i in x) {
            temp[[k]]<- log(i/(1-i))
            k <- k + 1
            }
            temp1 <- Reduce("+",temp)
            output <- temp1
            return(output)
            }
        },

        #EdMethod
        EdMethod = function(x) {
            if (self.method == "Ed"){
            k <- 1
            Len<- length(x)
            temp <-vector("list",Len)
            for (i in x) {
            temp[[k]]<- i
            k <- k + 1
            }
            temp1 <- Reduce("+",temp)
            output <- temp1
            return(output)
            }
        },

        #StoufferMethod
        StoufferMethod = function(x){
            if (self.method == "Stouffer"){
            k <- 1
            Len<- length(x)
            temp <-vector("list",Len)
            for (i in x) {
            temp[[k]]<- qnorm(i) #inverse CDF
            k <- k + 1
            }
            temp1 <- Reduce("+",temp)
            output <- temp1
            return(output)
            }
        },

        #TippettMethod
        TippettMethod = function(x){
            if (self.method == "Tippett"){
            temp <- Reduce(min,x)
            output <- temp
            return(output)
            }
        }
    ))
}

#Fisher, Pearson, Ed, Stouffer, George, Tippett
my_object <- myClass("Perason")
Output <- my_object$InfinitePs(0.1,0.3,.7)
print(my_object$PearsonsMethod(Output))

#Test
my_object <- myClass("Stouffer")
#random generator 10,12,15,18,20 N(mu,sigma^2) various values of mu and sigma^2
    mu <- sample(0:10,1)
    sigma <- sample(0:10,1)
    List <- list(10,12,15,18,20) #sample size
    for (x in List){
        Various <- rnorm(x, mean=mu, sd=sigma)
        Pvalues = pnorm(Various)
        Output = my_object$InfinitePs(Pvalues)
        #Get P values and combine
        Final <- my_object$StoufferMethod(Output)
        #print(Final)
        #SignOrNot = A.DetermineSig(Final)
    }
    #Get P values and Combine

    #random generator 10,12,15,18,20 t-statistic N(0,sigma^2)
    #Based on t-statistic each sample to test mu = 0. get P values and combine
    #mu <- 0
    #sigma <- sample(1:10,1)
    List <- list(10,12,15,18,20) #sample size
    PvalsFromPaper <- list(0.585,0.76,0.365,0.905,0.08,0.265,0.405,0.76,0.1,0.25,0.185,0.115,0.525,0.035,0.65,0.035,0.075,0.01,0.205,0.43,0.52,0.435,0.12)
    
    #my_object <- myClass("Tippett")
    for (x in List){
        Various <- rt(x, x-1)
        Pvalues = pt(Various, x-1)
        Output = my_object$InfinitePs(Pvalues)
        #print(Output)
        #Get P values and combine
        Final <- my_object$StoufferMethod(Output)
        print(Final)
        #SignOrNot = A.DetermineSig(Final)
    }
    
    #Testing new Paper Sheng and Cheng 
    my_object <- myClass("Stouffer")
    Final <- my_object$StoufferMethod(PvalsFromPaper)
    print(Final)

    my_object <- myClass("Fisher")
    Final <- my_object$FishersMethod(PvalsFromPaper)
    print(Final)
    #Data dataframes from the EmpricialBrownsMethod package
    print(try(data(package = "metap") ))
    


