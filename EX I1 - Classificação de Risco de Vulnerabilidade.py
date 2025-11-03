# I1: Classificação de Risco de Vulnerabilidade

# 1. Criar a variável com o score da vulnerabilidade
cvss_score = 7.8  # Valor do CVSS (Common Vulnerability Scoring System) que indica a gravidade da vulnerabilidade

# 2. Classificar o risco usando if-elif-else e operadores lógicos
if cvss_score >= 9.0:
    # Caso o score seja 9.0 ou maior, risco é crítico
    categoria = "Risco Crítico"
    acao = "Ação imediata: aplicar patch de segurança urgente."
elif cvss_score >= 7.0 and cvss_score < 9.0:
    # Score entre 7.0 e 8.9 indica risco alto
    categoria = "Risco Alto"
    acao = "Corrigir vulnerabilidade o quanto antes."
elif cvss_score >= 4.0 and cvss_score < 7.0:
    # Score entre 4.0 e 6.9 indica risco médio
    categoria = "Risco Médio"
    acao = "Monitorar e planejar correção."
else:
    # Score menor que 4.0 indica risco baixo
    categoria = "Risco Baixo"
    acao = "Sem necessidade imediata de ação."

# 3. Exibir a categoria e a recomendação de ação
print(f"Categoria: {categoria}")
print(f"Recomendação: {acao}")
