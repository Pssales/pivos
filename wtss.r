library(wtss)
server <- wtss::WTSS("http://www.esensing.dpi.inpe.br/wtss/")

df <- read.csv(file = "C:/Users/Camila/Desktop/LC8_SRgreenest_pivots_merged_polygon/output_pivos_ok_coordenadas.csv", header = TRUE, sep = ",")

lista <- list()


  for(i in 1:length(df[,1])){
    time_series <- wtss::timeSeries(server, coverages = "MOD13Q1", attributes=c("ndvi"),
                                    latitude=as.numeric(df[i,2]), longitude=as.numeric(df[i,1]), start_date="2017-11-01", end_date="2018-04-01")
    lista[[i]] <- c(time_series$MOD13Q1$attributes)
  }

data <- data.frame(matrix(unlist(lista), nrow=length(lista), byrow=T))
names(lista[[0]])
write.csv(data,'C:/Users/Camila/Desktop/LC8_SRgreenest_pivots_merged_polygon/Serie_output_pivos_ok_coordenadas.csv', row.names = FALSE)

print(lista)
