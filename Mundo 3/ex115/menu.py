from cores import cores
design = f"""
{cores[2] + '-' * 30 + cores[4]}
{ cores[1] + 'MENU PRINCIPAL'.center(30) + cores[4]}
{cores[2] +'-' * 30 + cores[4]}

\033[92m[1]\33[0m \033[93mVer Pessoas Cadastradas\33[0m
\033[92m[2]\33[0m \033[93mCadastar Nova Pessoa\33[0m
\033[92m[3]\33[0m \033[93mSair do Sistema\33[0m
"""