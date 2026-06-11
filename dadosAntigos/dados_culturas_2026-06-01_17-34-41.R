# ==================================================
# Script de dados gerado automaticamente pelo Python
# ==================================================

vetor_culturas <- c("Café", "Feijao", "Café", "Feijao")
vetor_areas <- c(11250.000, 100000.000, 6750.000, 20000.000)
vetor_insumos <- c(540.000, 675.000, 84.000, 44.800)

# Criando a tabela estatística (Data Frame)
df_culturas <- data.frame(
  Cultura = vetor_culturas,
  Area_m2 = vetor_areas,
  Insumo_kg = vetor_insumos
)

# Comandos prontos para análise:
print(df_culturas)
summary(df_culturas)
