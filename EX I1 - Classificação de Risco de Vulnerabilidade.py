cvss_score = 7.8
if cvss_score >= 9.0: 
 categoria = "Risco Crítico"
 acao = "Imediata, aplicar patch de segurança urgente!"
elif cvss_score >= 7.0 and cvss_score <9.0: 
 categoria = "Risco Alto"
 acao = "Corrigir vulnerabilidade o quanto antes!"
elif cvss_score >= 4.0 and cvss_score < 7.0: 
  categoria = "Risco Médio"
  acao = "Monitorar e planejar correção."
else:
  categoria = "Risco Baixo"
  acao = "Sem necessidade imediata de ação."

print(f"Categoria: {categoria}")
print(f"Recomendação: {acao}")