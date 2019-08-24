library(wtss)
server <- wtss::WTSS("http://www.esensing.dpi.inpe.br/wtss/")

df <- read.csv(file = "C:/Users/Camila/Desktop/pivos/output_coordenadas.csv", header = TRUE, sep = ",")

time_series <- wtss::timeSeries(server, coverages = "MOD13Q1", attributes=c("evi")
                                ,latitude=as.numeric(df[1,2]), longitude=as.numeric(df[1,1]), start_date="2017-02-01", end_date="2018-02-01")
plot (time_series$MOD13Q1$attributes$evi)
print(names(time_series$MOD13Q1$attributes$evi[0]))
print(fromJSON(time_series))
typeof(time_series$MOD13Q1$attributes)
print(time_series$MOD13Q1$attributes)



lista <- list()

for(i in 1:length(df[,1])){
  time_series <- wtss::timeSeries(server, coverages = "MOD13Q1", attributes=c("evi"),
                                  latitude=as.numeric(df[i,2]), longitude=as.numeric(df[i,1]), start_date="2017-02-01", end_date="2018-02-01")
  lista[[i]] <- c(time_series$MOD13Q1$attributes)
}
print(lista)

data <- data.frame(matrix(unlist(lista), nrow=length(lista), byrow=T))
names(lista[[0]])
write.csv(data,'C:/Users/Camila/Desktop/series.csv', row.names = FALSE)
