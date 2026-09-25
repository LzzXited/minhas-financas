# Minhas Finanças

App Android simples e offline para organizar as finanças pessoais.

## Funções

- **Receitas e despesas**: lançamentos com valor, descrição, categoria e data. Também dá para repetir por vários meses (parcelas e contas fixas).
- **Saldo**: saldo acumulado e resultado do mês, com navegação entre meses.
- **Orçamento por categoria**: limite mensal por categoria, com aviso ao chegar em 80% e ao estourar.
- **Relatórios**: despesas por categoria, receitas × despesas dos últimos 6 meses, evolução do saldo em 12 meses e resumo do mês.
- **Metas de economia**: valor-alvo, prazo e quanto guardar por mês.
- **Backup**: exportar e importar os dados (arquivo ou texto).
- Tema claro e escuro automático. Os dados ficam só no aparelho, sem conta e sem internet.

## Como instalar

1. Abra a página de [Releases](../../releases/latest) pelo celular.
2. Baixe o arquivo `MinhasFinancas.apk`.
3. Abra o arquivo. Se o Android pedir, permita instalar apps de fontes desconhecidas.

## Atualizações

A cada alteração enviada para a branch `main`, o GitHub Actions gera um novo APK e publica uma nova release automaticamente.

> **Importante:** antes de instalar uma versão nova, use **Mais → Exportar backup**. Se o Android recusar a atualização por conflito de assinatura, desinstale a versão antiga, instale a nova e importe o backup.

## Estrutura

- `index.html`: o app inteiro (HTML, CSS e JavaScript, sem dependências externas).
- `capacitor.config.json` e `package.json`: configuração do [Capacitor](https://capacitorjs.com), que empacota o app para Android.
- `make_icon.py`: gera o ícone do app durante o build.
- `.github/workflows/build-apk.yml`: gera o APK na nuvem e publica na página de Releases.
