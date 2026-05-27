# Marcio Soares Ferreira — Contexto Profissional Completo

> Este documento é a base de conhecimento usada pelo assistente do portfólio. Contém
> informações detalhadas sobre formação, carreira, projetos, conquistas técnicas e
> publicações de Marcio Ferreira.

---

## Identidade & Posicionamento

- **Nome completo:** Marcio Soares Ferreira
- **Título atual:** Cientista de Dados Sênior · Ph.D.
- **Especialidade:** Engenharia de IA Agêntica — LangGraph, AWS Bedrock, MCP Servers
- **Localização:** Manaus, Brasil (disponível para remoto)
- **Idiomas:** Português (nativo), Inglês (profissional)
- **E-mail:** marciosferreira@yahoo.com.br
- **LinkedIn:** https://www.linkedin.com/in/marcio-soares-ferreira
- **GitHub:** https://github.com/marciosferreira
- **YouTube:** https://www.youtube.com/@dr.marcio-ferreira

### Tagline / posicionamento

> "Agentes autônomos que operam em produção — do LangGraph à linha de fábrica."

Mais de 10 anos de rigor científico (EMBL-EBI Cambridge e INPA) aplicados à
engenharia de IA industrial. Projeta e coloca em produção arquiteturas multi-agente
com LangGraph, AWS Bedrock e MCP Servers. Histórico comprovado de **30–50% de
redução no consumo de tokens** em produção e observabilidade completa via
Langfuse/LangSmith. Autor de aproximadamente 20 publicações indexadas.

---

## Stack Técnico Principal

- **Frameworks de Agentes:** LangChain, LangGraph, MCP Servers
- **LLMs em produção:** AWS Bedrock (Claude, Llama), Llama on-premise (quantizado)
- **Recuperação & RAG:** FAISS, embeddings HuggingFace, busca semântica escalável
- **Observabilidade:** Langfuse, LangSmith (tracing, evals, benchmarking em produção)
- **Linguagens:** Python (avançado), SQL
- **Visão Computacional:** OpenCV, processamento digital de sinais
- **ML clássico:** Scikit-Learn, TensorFlow, Keras (LSTM/RNN)
- **Infraestrutura:** Linux, HPC, ambientes Docker, sandboxes isolados
- **Engenharia de contexto:** otimização agressiva de tokens, system prompts versionados

---

## Experiência Profissional

### Jul 2025 — presente: Cientista de Dados — FIT (Instituto de Tecnologia), Manaus, Brasil

Responsável pelo projeto e implantação de sistemas multi-agente para o setor
industrial. Atividades:

- **Arquitetura multi-agente com LangGraph** para análise de telemetria industrial
  e dados estruturados de produção (orquestrador + sub-agentes ReAct + StateGraph
  determinístico).
- **RAG com FAISS** correlacionando métricas em tempo real com logs históricos,
  reduzindo significativamente alucinações em diagnósticos de falhas.
- **MCP Servers em Python** desacoplando acesso a dados (SQL/NoSQL) da lógica
  dos modelos — protocolo aberto, reutilizável entre projetos.
- **Engenharia de contexto avançada:** alcançou redução de **30–50% no consumo
  de tokens** na AWS Bedrock através de poda de contexto, sumarização agressiva
  de histórico e roteamento dinâmico para modelos menores quando apropriado.
- **Observabilidade completa via Langfuse:** tracing distribuído, benchmarking
  contínuo e avaliação qualitativa em produção (LLM-as-judge + métricas custom).

**Projeto destaque:** Industry Control — agente que substitui rotinas manuais
de gerentes de manufatura (análise de OEE, paradas não planejadas, geração de
relatórios, agendamento de tarefas recorrentes em sandbox isolado). Demo ao
vivo: https://interview-demo-industry.b60gda.easypanel.host/

### Nov 2024 — Mai 2025: Analista de Machine Learning — Venturus, Manaus, Brasil

- **Arquitetura RAG on-premise com LLMs locais** (Llama quantizado) — zero
  exposição de dados sensíveis a APIs externas, atendendo requisitos rígidos de
  compliance e privacidade de dados industriais.
- **Migração de pipelines lineares LangChain para sistemas stateful com LangGraph**
  (memória persistente, ramificações condicionais, recuperação de erros, retry com
  backoff inteligente).
- **Observabilidade com LangSmith** para tracing, debugging e evals em todo o
  fluxo generativo.
- **Busca semântica de alta escala** com embeddings HuggingFace + FAISS sobre
  grandes corpora documentais corporativos.

### Fev 2021 — Fev 2024: Cientista de Dados — European Bioinformatics Institute (EMBL-EBI), Cambridge, Reino Unido

Atuação em ciência de dados aplicada à biologia computacional em um dos
principais institutos de bioinformática do mundo.

- **Algoritmos de object tracking e processamento digital de sinais** em Python/OpenCV
  para detecção automatizada de frequência cardíaca em vídeos de alta resolução de
  embriões (zebrafish).
- **Pipelines escaláveis em infraestrutura Linux/HPC** para análise de imagem
  biológica em larga escala.
- **Publicação científica revisada por pares** no journal *Bioinformatics* (Oxford
  Academic) — DOI: 10.1093/bioinformatics/btae664. Disponível em
  https://academic.oup.com/bioinformatics/article/40/12/btae664/7885156

### Jan 2016 — Jan 2021: Pesquisador Pós-Doutorado — INPA (Instituto Nacional de Pesquisas da Amazônia), Manaus, Brasil

- **Redes neurais LSTM/RNN em TensorFlow/Keras** para modelagem preditiva de
  séries temporais e classificação comportamental de organismos amazônicos.
- **PCA e clustering** para engenharia de features em dados biológicos de alta
  dimensionalidade.
- **Integração de sensores IoT com visão computacional** em pipelines multimodais
  validados estatisticamente.
- Publicação no periódico *FACETS* — DOI: 10.1139/facets-2023-0221.

---

## Formação Acadêmica

- **Ph.D. em Biologia Computacional** — INPA (2011 – 2015)
- **Mestrado em Biologia Computacional** — INPA (2004 – 2006)
- **Bacharelado em Ciências Biológicas** — UNIARA (1999 – 2003)
- **Tecnólogo em Ciência de Dados** — Estácio (2024 – 2026)

---

## Meus Projetos em Destaque

### 1. Industry Control — Demo Industry Dashboard

**Stack:** LangGraph, LangChain, AWS Bedrock, FAISS, Python, SQLite, FastAPI,
SSE (Server-Sent Events).

**O que faz:** Sistema multi-agente que substitui o trabalho rotineiro de
gerentes de manufatura. Um usuário conversa em linguagem natural e o agente:

- Analisa indicadores em tempo real (OEE, paradas não planejadas, throughput).
- Gera relatórios em PDF e Excel sob demanda.
- Cria gráficos e visualizações.
- Agenda tarefas recorrentes — escreve, testa e versiona código Python que
  roda em sandbox isolado, com correção automática em até 3 tentativas em
  caso de erro.
- Envia alertas por e-mail e notificações via `ctx.notify()`.

**Arquitetura:**
- **Orquestrador** (ReAct) decide qual sub-agente acionar.
- **Sub-Agente Analista** (ReAct) consulta dados e gera artefatos.
- **SchedulingGraph** (StateGraph determinístico) cria/edita/testa/versiona
  código de tarefas agendadas.
- **Sub-Agente Scheduling** (ReAct) gerencia CRUD de tarefas.
- **Daemon** executa tarefas a cada 60s em ambiente isolado e seguro.
- **SQLite** para persistência; **Langfuse** para observabilidade.

**Demo:** https://interview-demo-industry.b60gda.easypanel.host/

### 2. Acing Interviews

**O que faz:** Plataforma de simulação de entrevistas com agente de IA que
oferece perguntas específicas ao cargo, feedback instantâneo (texto e voz) e
scorecards personalizados.

**Site:** https://acinginterviews.com/

### 3. Fish Behaviour Detection

**O que faz:** Análise de movimento e comportamento de peixes via Python,
Jupyter e processamento de vídeo. Repositório aberto com notebooks e scripts.

**GitHub:** https://github.com/marciosferreira/fish_behaviour_detection

### 4. Publicação em Bioinformatics (Oxford Academic)

Trabalho de análise e bioinformática publicado na revista *Bioinformatics* da
Oxford Academic, fruto da atuação no EMBL-EBI Cambridge.

**Link:** https://academic.oup.com/bioinformatics/article/40/12/btae664/7885156

---

## Conteúdo Técnico (YouTube)

Canal: https://www.youtube.com/@dr.marcio-ferreira

Vídeos publicados:

1. **Entendendo o LangChain de verdade, e sem tutorial** — https://youtu.be/WNO4oMGtYOM
2. **Como um Editor de Código com IA Funciona por Dentro** — https://youtu.be/N-mFfjFTH2k
3. **LangGraph — Os 7 conceitos que você precisa saber** — https://youtu.be/a2ZKkoedJp4
4. **Orquestração de agentes de IA: do Loop ReAct à produção** — https://youtu.be/0FYTz2IsObc

---

## Conquistas e Diferenciais

- **30–50% de redução no consumo de tokens** em produção na AWS Bedrock através
  de engenharia de contexto agressiva.
- **~20 publicações científicas indexadas** ao longo da carreira acadêmica.
- **Passagem por instituições de referência** internacional (EMBL-EBI Cambridge)
  e nacional (INPA Manaus).
- **Migração bem-sucedida** de pipelines LangChain lineares para sistemas
  LangGraph stateful em ambiente corporativo (Venturus).
- **Implantação de RAG on-premise** com LLMs locais para casos de uso com
  restrições de compliance.
- **Autor de canal técnico** no YouTube com conteúdo educacional sobre
  LangChain, LangGraph e arquiteturas de agentes.

---

## Estilo de Trabalho e Perfil

- Rigor científico aplicado à engenharia: tudo é mensurado, observado e
  validado em produção.
- Forte preferência por arquiteturas explícitas e determinísticas onde
  possível (StateGraph), reservando ReAct para tarefas que realmente exigem
  raciocínio livre.
- Foco em sistemas que substituem trabalho manual real — não em demos ou
  provas-de-conceito.
- Documentação técnica detalhada e código versionado.
- Combinação de profundidade científica (Ph.D., ~20 papers) com pragmatismo
  industrial (entrega contínua em produção).

---

## O que Marcio busca profissionalmente

- Posições sêniores em IA Agêntica / AI Lead / Senior AI Engineer.
- Projetos com escopo real de produção (não apenas R&D).
- Empresas que valorizam observabilidade, engenharia de contexto e arquiteturas
  multi-agente bem desenhadas.
- Modalidades: CLT, PJ ou Consultoria. Remoto preferencialmente, com base em
  Manaus, Brasil.

---

## Como entrar em contato

- **E-mail:** marciosferreira@yahoo.com.br
- **LinkedIn:** https://www.linkedin.com/in/marcio-soares-ferreira

Para discussões técnicas, projetos colaborativos ou oportunidades, o canal
preferencial é o LinkedIn ou o e-mail acima.
