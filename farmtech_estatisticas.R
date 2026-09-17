# FarmTech Solutions - Estatisticas basicas
# Disciplina: Dev - FIAP
#
# Requisito (g): usa os dados gerados pelo app em Python (dados_culturas.csv)
# para calcular media e desvio padrao da area plantada e do insumo utilizado.

# Le o arquivo CSV exportado pelo Python (precisa estar na mesma pasta)
if (!file.exists("dados_culturas.csv")) {
  stop("Arquivo 'dados_culturas.csv' nao encontrado. Rode o farmtech.py primeiro e coloque este script R na mesma pasta.")
}

dados <- read.csv("dados_culturas.csv", stringsAsFactors = FALSE)

cat("===== FarmTech Solutions - Estatisticas =====\n\n")
cat("Dados carregados:\n")
print(dados)

# Calcula media e desvio padrao da area plantada (coluna area_m2)
media_area <- mean(dados$area_m2)
desvio_area <- sd(dados$area_m2)

# Calcula media e desvio padrao do insumo utilizado (coluna total_insumo_litros)
media_insumo <- mean(dados$total_insumo_litros)
desvio_insumo <- sd(dados$total_insumo_litros)

cat("\n--- Area de plantio (m2) ---\n")
cat(sprintf("Media: %.2f m2\n", media_area))
cat(sprintf("Desvio padrao: %.2f m2\n", desvio_area))

cat("\n--- Insumo utilizado (litros) ---\n")
cat(sprintf("Media: %.2f litros\n", media_insumo))
cat(sprintf("Desvio padrao: %.2f litros\n", desvio_insumo))
