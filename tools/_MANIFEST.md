# Agent library — 256 agents

Source: `.agents/agents/<slug>.md` — one file per agent, grouped by category below.

Total: **256** agents in **16** categories.

## code (16)

- `code-frontend` — Frontend Developer — Use when a user-facing web interface must be built or changed. Owns components, state and the browser-facing layer. Load on 'frontend', 'React', 'UI component', 'build the page', 'component'.
- `code-backend` — Backend Developer — Use when server-side logic, data access or business rules must be implemented. Owns services, endpoints and persistence. Load on 'backend', 'API endpoint', 'server logic', 'database query'.
- `code-fullstack` — Fullstack Developer — Use when a feature spans browser and server and one owner should carry it end to end. Load on 'full stack', 'end to end feature', 'wire it up', 'feature from UI to DB'.
- `code-mobile` — Mobile Developer — Use when an app must ship to iOS or Android. Owns screens, navigation, native APIs and store constraints. Load on 'mobile app', 'iOS', 'Android', 'React Native', 'Flutter'.
- `code-desktop` — Desktop App Developer — Use when a native or cross-platform desktop application must be built. Owns windows, menus, filesystem access, packaging and updates. Load on 'desktop app', 'Electron', 'Tauri', 'native app', 'installer'.
- `code-api` — API Designer — Use when a service must expose an interface others will consume. Designs resources, contracts, versioning and errors. Load on 'API design', 'REST', 'GraphQL', 'endpoint contract', 'OpenAPI'.
- `code-refactor` — Refactoring Specialist — Use when code works but is hard to change. Improves structure without changing behaviour. Load on 'refactor', 'clean this up', 'this is a mess', 'reduce duplication'.
- `code-migration` — Code Migration Engineer — Use when code must move to a new language, framework or major version. Plans and executes the migration with a rollback. Load on 'migrate', 'upgrade to v2', 'port to', 'move off'.
- `code-reviewer` — Code Reviewer — Use when a change needs a critical read before it lands. Reviews for correctness, clarity, safety and fit. Load on 'review this', 'check my code', 'PR review', 'code review'.
- `code-debugger` — Debugging Specialist — Use when something is broken and the cause is unknown. Reproduces, isolates and fixes the root cause. Load on 'debug', 'it is broken', 'why does this fail', 'find the bug'.
- `code-perf` — Performance Engineer — Use when something is slow or resource-hungry. Measures, profiles and optimizes with evidence. Load on 'too slow', 'performance', 'optimize', 'latency', 'profile this'.
- `code-architect` — Software Architect — Use when a system's structure must be decided before it is built. Owns boundaries, contracts, trade-offs and evolution. Load on 'architecture', 'how should this be structured', 'system design', 'modules'.
- `code-legacy` — Legacy Code Archaeologist — Use when unfamiliar old code must be understood or changed safely. Maps behaviour, finds the seams and adds tests. Load on 'legacy code', 'nobody understands this', 'old codebase', 'before my time'.
- `code-integration` — Integration Engineer — Use when two systems must talk to each other. Owns the contract, the adapter and the failure handling. Load on 'integrate', 'connect to', 'third-party API', 'webhook', 'SSO'.
- `code-cli` — CLI Tool Developer — Use when a task should be runnable from the terminal. Owns arguments, output, exit codes and composability. Load on 'CLI', 'command line tool', 'script', 'terminal command'.
- `code-game` — Game Developer — Use when a playable game must be built. Owns the loop, input, physics, state and feel. Load on 'game', 'playable', 'game loop', 'levels', 'canvas game'.

## ui (16)

- `ui-designer` — UI Designer — Use when an interface's look and layout must be designed. Owns hierarchy, spacing, components and visual polish. Load on 'design the UI', 'make it look good', 'layout', 'mockup'.
- `ux-designer` — UX Designer — Use when a flow or interaction must be designed around real user goals. Owns journeys, information architecture and friction. Load on 'UX', 'user flow', 'journey', 'information architecture'.
- `ui-design-system` — Design System Architect — Use when a product needs consistent, reusable interface primitives. Owns tokens, components and their rules. Load on 'design system', 'component library', 'tokens', 'style guide'.
- `ui-motion` — Motion Designer — Use when an interface needs motion that clarifies rather than decorates. Owns transitions, easing and choreography. Load on 'animation', 'transition', 'motion', 'micro-interaction'.
- `ui-brand` — Brand Designer — Use when a product or company needs a visual identity. Owns logo, palette, type and voice. Load on 'brand', 'logo', 'identity', 'brand guidelines'.
- `ui-illustrator` — Illustrator — Use when a product needs original illustration. Owns style, composition and consistency across a set. Load on 'illustration', 'draw', 'spot art', 'empty state art'.
- `ui-icon` — Icon Designer — Use when a product needs a coherent icon set. Owns grid, stroke, weight and metaphor. Load on 'icons', 'icon set', 'glyph', 'symbols'.
- `ui-typography` — Typography Specialist — Use when text hierarchy and readability must be fixed. Owns type scale, pairing, spacing and rhythm. Load on 'typography', 'fonts', 'type scale', 'text is unreadable'.
- `ui-color` — Color Specialist — Use when a palette must be defined or corrected. Owns hue, contrast and semantic color. Load on 'color palette', 'colors', 'contrast', 'dark mode'.
- `ui-accessibility` — Accessibility Designer — Use when an interface must work for everyone, including assistive tech. Owns semantics, keyboard, contrast and screen-reader flow. Load on 'accessibility', 'a11y', 'WCAG', 'screen reader', 'keyboard nav'.
- `ui-responsive` — Responsive Layout Specialist — Use when a layout must hold up across screen sizes and inputs. Owns breakpoints, fluid type and reflow. Load on 'responsive', 'mobile layout', 'breakpoints', 'it breaks on small screens'.
- `ui-prototype` — Prototyper — Use when an idea must be made tangible to be judged. Builds the fastest thing that answers the question. Load on 'prototype', 'mock it up', 'proof of concept', 'clickable demo'.
- `ui-user-research` — User Researcher — Use when decisions need evidence about real users. Plans studies, runs sessions and synthesizes findings. Load on 'user research', 'interview users', 'usability test', 'what do users want'.
- `ui-content` — UX Writer — Use when interface text must be clear and useful. Owns labels, errors, empty states and microcopy. Load on 'UX writing', 'microcopy', 'error message', 'button label', 'copy'.
- `ui-3d` — 3D Designer — Use when a scene, model or spatial interface must be designed. Owns geometry, materials, lighting and camera. Load on '3D', 'Three.js scene', 'model', 'lighting', 'render'.
- `ui-visual-qa` — Visual QA Reviewer — Use when a built interface must be checked against its design. Compares rendering, spacing and states pixel by pixel. Load on 'visual QA', 'does this match the design', 'pixel check', 'design review'.

## test (16)

- `test-unit` — Unit Test Engineer — Use when a single unit of logic needs a fast, isolated test. Load on 'unit test', 'test this function', 'cover this branch'.
- `test-integration` — Integration Test Engineer — Use when components must be proven to work together. Tests real wiring against real or realistic dependencies. Load on 'integration test', 'test the wiring', 'does this work together'.
- `test-e2e` — E2E Test Engineer — Use when a user journey must be proven end to end in a real browser. Load on 'e2e', 'end to end test', 'Playwright', 'Cypress', 'user journey test'.
- `test-performance` — Performance Test Engineer — Use when speed, throughput or resource use must be measured and defended. Load on 'performance test', 'benchmark', 'how fast is it', 'throughput'.
- `test-security` — Security Test Engineer — Use when a system must be tested for vulnerabilities, not just reviewed. Load on 'security test', 'pen test the app', 'SQL injection', 'XSS test', 'OWASP'.
- `test-accessibility` — Accessibility Tester — Use when an interface must be verified against WCAG and assistive tech. Load on 'accessibility test', 'a11y audit', 'screen reader test', 'WCAG check'.
- `test-automation` — Test Automation Engineer — Use when manual checks should become a reliable automated suite. Load on 'automate the tests', 'test framework', 'test harness', 'CI test setup'.
- `test-manual` — Manual QA Engineer — Use when a human eye is needed to judge quality. Explores, checks edge cases and reports clearly. Load on 'manual test', 'QA', 'test this build', 'check the app'.
- `test-api` — API Tester — Use when an HTTP or RPC interface must be verified. Checks contracts, status codes, auth and edge cases. Load on 'API test', 'test the endpoint', 'Postman', 'contract check'.
- `test-mobile` — Mobile QA Engineer — Use when an app must be verified on real devices and networks. Load on 'mobile QA', 'test on device', 'iOS test', 'Android test'.
- `test-load` — Load Test Engineer — Use when a system must survive real traffic. Models load, runs it and finds the breaking point. Load on 'load test', 'stress test', 'will it scale', 'concurrency'.
- `test-chaos` — Chaos Engineer — Use when resilience must be proven, not assumed. Injects real failures and checks recovery. Load on 'chaos test', 'fault injection', 'resilience', 'what if it fails'.
- `test-contract` — Contract Test Engineer — Use when two services must agree on an interface. Pins the contract and verifies both sides. Load on 'contract test', 'consumer-driven contract', 'Pact', 'API compatibility'.
- `test-exploratory` — Exploratory Tester — Use when a feature needs adversarial, unscripted investigation. Load on 'exploratory test', 'try to break it', 'poke around', 'find edge cases'.
- `test-regression` — Regression Test Owner — Use when past bugs must never return. Owns the regression suite and its growth. Load on 'regression test', 'did we break anything', 'add a test for this bug', 'guard this fix'.
- `test-qa-lead` — QA Lead — Use when test strategy and quality gates must be owned. Load on 'QA strategy', 'test plan', 'quality gate', 'release criteria'.

## sec (16)

- `sec-appsec` — AppSec Engineer — Use when an application's code and design must be secured. Load on 'appsec', 'secure this app', 'security review', 'fix the vulnerability'.
- `sec-pentest` — Penetration Tester — Use when a system must be attacked deliberately to find exploitable flaws. Load on 'pen test', 'pentest', 'find vulnerabilities', 'attack surface'.
- `sec-threat-model` — Threat Modeler — Use when a system's design must be examined for what could go wrong. Load on 'threat model', 'STRIDE', 'what could go wrong', 'attack paths'.
- `sec-secrets` — Secrets & Credentials Engineer — Use when credentials, keys or tokens must be managed safely. Load on 'secrets', 'API keys', 'rotate credentials', 'leaked key', 'vault'.
- `sec-cloud` — Cloud Security Architect — Use when cloud infrastructure must be secured by design. Load on 'cloud security', 'IAM policy', 'S3 bucket', 'network security', 'cloud hardening'.
- `sec-supply-chain` — Supply Chain Security Engineer — Use when dependencies and build artifacts must be trusted. Load on 'supply chain', 'dependency audit', 'SBOM', 'is this package safe'.
- `sec-incident` — Incident Responder — Use when a security incident is happening or suspected. Contains, investigates and recovers. Load on 'incident', 'we are breached', 'security incident', 'contain this'.
- `sec-forensics` — Digital Forensics Analyst — Use when a system must be examined after an event to reconstruct what happened. Load on 'forensics', 'what happened', 'timeline', 'evidence analysis'.
- `sec-crypto` — Cryptography Engineer — Use when encryption, signing or hashing must be implemented or reviewed. Load on 'crypto', 'encryption', 'hashing', 'signing', 'TLS'.
- `sec-identity` — Identity & Access Engineer — Use when authentication, authorization or identity must be designed. Load on 'auth', 'SSO', 'OAuth', 'RBAC', 'who can do what'.
- `sec-privacy` — Privacy Engineer — Use when personal data is collected, stored or shared. Load on 'privacy', 'GDPR', 'PII', 'data retention', 'consent'.
- `sec-compliance` — Compliance Engineer — Use when a system must meet a standard or regulation. Load on 'compliance', 'SOC 2', 'ISO 27001', 'HIPAA', 'audit readiness'.
- `sec-vuln` — Vulnerability Analyst — Use when findings and CVEs must be triaged and prioritized. Load on 'vulnerability', 'CVE', 'triage findings', 'patch priority'.
- `sec-soc` — SOC Analyst — Use when security events must be monitored and triaged. Load on 'SOC', 'alert triage', 'SIEM', 'is this malicious'.
- `sec-red-team` — Red Team Operator — Use when defenses must be tested by a realistic adversary. Load on 'red team', 'adversary simulation', 'assume breach', 'test detection'.
- `sec-security-architect` — Security Architect — Use when security must be designed into a system from the start. Load on 'security architecture', 'secure design', 'defense in depth', 'zero trust'.

## data (16)

- `data-engineer` — Data Engineer — Use when data must be moved, shaped and made reliable. Owns pipelines, schemas and storage. Load on 'data pipeline', 'ETL', 'data ingestion', 'move this data'.
- `data-analyst` — Data Analyst — Use when a question must be answered with data. Load on 'analyze this', 'what do the numbers say', 'report', 'dashboard data'.
- `data-scientist` — Data Scientist — Use when a problem needs modelling or statistical inference. Load on 'model this', 'predict', 'statistics', 'experiment analysis'.
- `data-warehouse` — Data Warehouse Architect — Use when analytical data must be organized for query at scale. Load on 'warehouse', 'dimensional model', 'star schema', 'OLAP'.
- `data-pipeline` — Pipeline Engineer — Use when a data flow must be built and kept running. Load on 'build the pipeline', 'orchestration', 'Airflow', 'DAG', 'schedule this'.
- `data-quality` — Data Quality Engineer — Use when data must be trusted, not just present. Load on 'data quality', 'validate the data', 'bad data', 'data checks'.
- `data-modeler` — Data Modeler — Use when the structure of data must be designed. Load on 'data model', 'ERD', 'schema design', 'entity relationship'.
- `data-visualization` — Data Visualization Engineer — Use when data must be shown so a human can act on it. Load on 'chart', 'visualization', 'dashboard', 'graph this', 'plot'.
- `data-bi` — BI Developer — Use when business reporting must be built and maintained. Load on 'BI', 'reporting', 'Looker', 'Power BI', 'business dashboard'.
- `data-etl` — ETL Developer — Use when data must be extracted, transformed and loaded reliably. Load on 'ETL', 'transform this data', 'load into', 'data load'.
- `data-streaming` — Streaming Data Engineer — Use when data must be processed continuously as it arrives. Load on 'streaming', 'Kafka', 'real-time data', 'event stream', 'CDC'.
- `data-governance` — Data Governance Lead — Use when data ownership, access and policy must be defined. Load on 'data governance', 'who owns this data', 'data policy', 'access control for data'.
- `data-catalog` — Data Catalog Owner — Use when people cannot find or understand the data that exists. Load on 'data catalog', 'metadata', 'where is this data', 'data discovery'.
- `data-migration` — Data Migration Engineer — Use when data must move between systems without loss. Load on 'data migration', 'move the data', 'import into', 'system migration'.
- `data-analytics` — Analytics Engineer — Use when the layer between raw data and BI must be owned. Load on 'analytics engineering', 'dbt', 'transform models', 'semantic layer'.
- `data-ml-data` — ML Data Engineer — Use when data for machine learning must be collected, labelled and served. Load on 'training data', 'feature store', 'label this data', 'data for ML'.

## ai (16)

- `ai-llm-engineer` — LLM Engineer — Use when a language model must be applied to a real product problem. Load on 'LLM', 'GPT', 'Claude API', 'build with an LLM', 'model integration'.
- `ai-rag` — RAG Pipeline Engineer — Use when answers must be grounded in a private corpus. Load on 'RAG', 'retrieval', 'ground it in our docs', 'vector search', 'knowledge base'.
- `ai-prompt` — Prompt Engineer — Use when model behaviour must be shaped by the prompt. Load on 'prompt', 'system prompt', 'make the model do X', 'prompt template'.
- `ai-fine-tune` — Fine-tuning Engineer — Use when a model must be specialized to a domain or format. Load on 'fine-tune', 'train the model', 'LoRA', 'custom model'.
- `ai-eval` — Model Evaluation Engineer — Use when model quality must be measured, not guessed. Load on 'evaluate the model', 'benchmark the LLM', 'is it better', 'eval set'.
- `ai-agent` — AI Agent Engineer — Use when a model must act in a loop with tools, not just answer. Load on 'agent', 'tool use', 'function calling', 'autonomous loop', 'agent loop'.
- `ai-multi-agent` — Multi-Agent Systems Architect — Use when several agents must work together on one goal. Load on 'multi-agent', 'agent orchestration', 'supervisor agent', 'agent team'.
- `ai-mcp` — MCP Server Builder — Use when a capability must be exposed to agents through MCP. Load on 'MCP server', 'model context protocol', 'expose a tool', 'MCP tool'.
- `ai-vector` — Vector Search Engineer — Use when similarity search over embeddings must be built. Load on 'vector database', 'embeddings', 'similarity search', 'semantic search'.
- `ai-inference` — Inference Optimization Engineer — Use when model serving must be faster or cheaper. Load on 'inference', 'serve the model', 'latency', 'quantization', 'GPU cost'.
- `ai-safety` — AI Safety Engineer — Use when a model's outputs or actions must be constrained. Load on 'AI safety', 'guardrails', 'prevent misuse', 'model alignment'.
- `ai-red-team` — AI Red Teamer — Use when a model or agent must be attacked to find weaknesses. Load on 'red team the model', 'jailbreak', 'prompt injection', 'attack the AI'.
- `ai-voice` — Voice AI Engineer — Use when speech must be recognized, generated or conversed with. Load on 'voice AI', 'speech to text', 'TTS', 'voice agent', 'transcription'.
- `ai-vision` — Computer Vision Engineer — Use when images or video must be interpreted. Load on 'computer vision', 'image recognition', 'detect objects', 'OCR', 'vision model'.
- `ai-nlp` — NLP Engineer — Use when text must be classified, extracted or generated at scale. Load on 'NLP', 'text classification', 'entity extraction', 'sentiment', 'text processing'.
- `ai-mlops` — MLOps Engineer — Use when models must be deployed, monitored and maintained. Load on 'MLOps', 'deploy the model', 'model monitoring', 'retrain', 'model registry'.

## ops (16)

- `ops-devops` — DevOps Automator — Use when manual operations should become automated and repeatable. Load on 'devops', 'automate deployment', 'pipeline', 'infrastructure automation'.
- `ops-sre` — Site Reliability Engineer — Use when a service's reliability must be defined and defended. Load on 'SRE', 'reliability', 'SLO', 'error budget', 'uptime'.
- `ops-platform` — Platform Engineer — Use when internal teams need a paved road to ship on. Load on 'platform', 'internal developer platform', 'golden path', 'self-service'.
- `ops-cloud` — Cloud Engineer — Use when infrastructure must be provisioned in a cloud. Load on 'cloud', 'AWS', 'GCP', 'Azure', 'provision infrastructure'.
- `ops-kubernetes` — Kubernetes Engineer — Use when workloads must run on Kubernetes. Load on 'kubernetes', 'k8s', 'pods', 'helm', 'cluster'.
- `ops-terraform` — Infrastructure as Code Engineer — Use when infrastructure must be declared, reviewed and versioned. Load on 'terraform', 'IaC', 'infrastructure as code', 'plan and apply'.
- `ops-ci` — CI/CD Engineer — Use when code must flow from commit to production automatically. Load on 'CI', 'CD', 'pipeline', 'GitHub Actions', 'build automation'.
- `ops-monitoring` — Observability Engineer — Use when a system's behaviour must be visible from the outside. Load on 'monitoring', 'observability', 'metrics', 'tracing', 'logging'.
- `ops-incident` — Incident Commander — Use when an outage must be run, not just fixed. Load on 'incident command', 'we are down', 'outage', 'coordinate the response'.
- `ops-oncall` — On-call Engineer — Use when a rotation must handle pages well. Load on 'on-call', 'pager', 'rotation', 'handle the alert'.
- `ops-capacity` — Capacity Planner — Use when growth must be met without over- or under-provisioning. Load on 'capacity', 'will it scale', 'how much do we need', 'growth planning'.
- `ops-network` — Network Engineer — Use when connectivity, routing or network security must be designed. Load on 'network', 'DNS', 'load balancer', 'firewall', 'VPC'.
- `ops-database` — Database Administrator — Use when a database must be run, tuned and protected. Load on 'database admin', 'DBA', 'database is slow', 'replication', 'backup the database'.
- `ops-backup` — Backup & Recovery Engineer — Use when data must survive loss. Load on 'backup', 'recovery', 'disaster recovery', 'restore point', 'RTO RPO'.
- `ops-cost` — Cloud Cost Optimizer — Use when cloud spend must be reduced without breaking things. Load on 'cloud cost', 'reduce spend', 'AWS bill', 'cost optimization'.
- `ops-release` — Release Engineer — Use when software must be released predictably. Load on 'release', 'versioning', 'ship it', 'release process', 'changelog and tag'.

## doc (16)

- `doc-technical-writer` — Technical Writer — Use when a concept or system must be explained clearly in writing. Load on 'write docs', 'document this', 'explain it', 'technical writing'.
- `doc-api-docs` — API Documentation Writer — Use when an API must be documented for its consumers. Load on 'API docs', 'document the endpoint', 'OpenAPI docs', 'reference docs'.
- `doc-readme` — README Author — Use when a project needs an entry point a stranger can follow. Load on 'README', 'write the readme', 'how do I run this'.
- `doc-changelog` — Changelog Curator — Use when a project's changes must be recorded for its users. Load on 'changelog', 'release notes', 'what changed', 'keep a changelog'.
- `doc-arch-doc` — Architecture Documenter — Use when a system's structure must be explained for the long term. Load on 'architecture doc', 'document the architecture', 'system overview', 'C4 diagram'.
- `doc-adr` — ADR Author — Use when a design decision must be recorded with its rationale. Load on 'ADR', 'architecture decision record', 'why did we choose this'.
- `doc-runbook` — Runbook Author — Use when an operator must act correctly under pressure. Load on 'runbook', 'operational procedure', 'how to fix this', 'playbook'.
- `doc-tutorial` — Tutorial Author — Use when a reader must learn by doing. Load on 'tutorial', 'getting started guide', 'walk me through it', 'step by step'.
- `doc-reference` — Reference Docs Author — Use when every option and behaviour must be documented precisely. Load on 'reference', 'document every option', 'API reference', 'config reference'.
- `doc-diagrams` — Diagram Author — Use when a system or flow must be shown visually. Load on 'diagram', 'draw the flow', 'sequence diagram', 'architecture diagram'.
- `doc-onboarding` — Onboarding Doc Author — Use when a new person must become productive quickly. Load on 'onboarding', 'new developer setup', 'getting started at the company'.
- `doc-style` — Documentation Style Editor — Use when a docs set must be consistent and readable. Load on 'docs style', 'edit the docs', 'consistency', 'style guide for docs'.
- `doc-translator` — Technical Translator — Use when documentation must cross a language boundary. Load on 'translate the docs', 'localization', 'another language', 'i18n docs'.
- `doc-knowledge-base` — Knowledge Base Curator — Use when answers to repeated questions must live somewhere findable. Load on 'knowledge base', 'FAQ', 'help center', 'document the answers'.
- `doc-release-notes` — Release Notes Writer — Use when a release must be communicated to users. Load on 'release notes', 'announce the release', 'what is new'.
- `doc-docs-reviewer` — Docs Reviewer — Use when documentation must be checked for accuracy and clarity. Load on 'review the docs', 'is this doc correct', 'docs review'.

## research (16)

- `research-web` — Web Researcher — Use when facts must be gathered from the open web. Load on 'research this', 'look it up', 'find sources', 'search the web'.
- `research-market` — Market Researcher — Use when a market, its size or its segments must be understood. Load on 'market research', 'market size', 'TAM', 'who is the market'.
- `research-user` — User Researcher — Use when decisions need evidence about real users. Load on 'user research', 'interview users', 'usability study', 'what do users need'.
- `research-competitive` — Competitive Analyst — Use when rivals and alternatives must be understood. Load on 'competitors', 'competitive analysis', 'who else does this', 'market landscape'.
- `research-technical` — Technical Researcher — Use when a technical approach, library or specification must be understood. Load on 'research this technology', 'how does X work', 'compare libraries', 'read the spec'.
- `research-academic` — Academic Researcher — Use when a question needs the scholarly literature. Load on 'papers', 'literature review', 'what does the research say', 'cite sources'.
- `research-data` — Data Researcher — Use when a question must be answered from datasets. Load on 'find data', 'dataset', 'open data', 'analyze this dataset'.
- `research-synthesist` — Research Synthesist — Use when many sources must become one coherent answer. Load on 'synthesize', 'summarize the research', 'pull this together', 'what does it all say'.
- `research-fact-checker` — Fact Checker — Use when claims must be verified before they are used. Load on 'fact check', 'is this true', 'verify this claim', 'check the numbers'.
- `research-source-validator` — Source Validator — Use when the trustworthiness of sources must be judged. Load on 'is this source reliable', 'source quality', 'can I trust this'.
- `research-trend` — Trend Analyst — Use when direction over time must be read from the noise. Load on 'trends', 'what is changing', 'where is this going', 'emerging'.
- `research-patent` — Patent Researcher — Use when prior art or IP landscape must be understood. Load on 'patents', 'prior art', 'IP search', 'freedom to operate'.
- `research-legal` — Legal Researcher — Use when rules, regulations or contracts must be researched. Load on 'legal research', 'what does the law say', 'regulation', 'contract terms'.
- `research-osint` — OSINT Analyst — Use when information must be gathered from public sources about an entity. Load on 'OSINT', 'open source intelligence', 'public records', 'background check'.
- `research-interviewer` — Interview Designer — Use when knowledge must be extracted from people. Load on 'interview guide', 'design the questions', 'expert interview', 'user interview script'.
- `research-brief` — Research Brief Writer — Use when research must be delivered so a decision can be made. Load on 'research brief', 'write up the research', 'decision memo', 'findings summary'.

## product (16)

- `product-manager` — Product Manager — Use when a product area needs an owner for what to build and why. Load on 'product manager', 'PM', 'own this product', 'what should we build'.
- `product-owner` — Product Owner — Use when a backlog must be ordered and kept ready. Load on 'product owner', 'backlog', 'sprint planning', 'accept the work'.
- `product-strategist` — Product Strategist — Use when a product needs a direction beyond the next release. Load on 'product strategy', 'where should the product go', 'vision', 'product direction'.
- `product-analyst` — Product Analyst — Use when product decisions need data. Load on 'product analytics', 'funnel analysis', 'retention', 'usage data'.
- `product-designer` — Product Designer — Use when a feature needs design from problem to polished interface. Load on 'product design', 'design this feature', 'end to end design'.
- `product-researcher` — Product Researcher — Use when product direction needs continuous user evidence. Load on 'product research', 'discovery', 'what should we build next', 'user needs'.
- `product-pm` — Program Manager — Use when many workstreams must land together. Load on 'program manager', 'cross-team coordination', 'dependencies', 'launch program'.
- `product-prioritizer` — Prioritization Lead — Use when everything is urgent and nothing is ordered. Load on 'prioritize', 'what first', 'RICE', 'backlog order'.
- `product-roadmap` — Roadmap Owner — Use when the plan beyond the next sprint must be communicated. Load on 'roadmap', 'quarters', 'product plan', 'what is coming'.
- `product-pricing` — Pricing Strategist — Use when a product must be priced and packaged. Load on 'pricing', 'how much', 'tiers', 'monetization', 'packaging'.
- `product-positioning` — Positioning Strategist — Use when a product must be described so the right people understand it. Load on 'positioning', 'value proposition', 'who is this for', 'messaging'.
- `product-launch` — Launch Manager — Use when a release must reach the market in a coordinated way. Load on 'launch', 'go to market', 'ship the announcement', 'release plan'.
- `product-growth` — Growth PM — Use when acquisition, activation or retention must move. Load on 'growth', 'activation', 'retention', 'funnel', 'conversion'.
- `product-experiment` — Experiment Designer — Use when a change should be proven rather than assumed. Load on 'A/B test', 'experiment', 'test this change', 'statistical significance'.
- `product-metrics` — Metrics Owner — Use when a team cannot tell whether the product is working. Load on 'metrics', 'north star', 'KPIs', 'how do we measure'.
- `product-feedback` — Feedback Synthesizer — Use when user feedback arrives from many channels and must be understood. Load on 'feedback', 'user complaints', 'support themes', 'voice of the customer'.

## biz (16)

- `biz-marketing` — Marketing Strategist — Use when a product must reach and convince a market. Load on 'marketing', 'go to market', 'campaign', 'demand generation'.
- `biz-content` — Content Marketer — Use when content must attract and educate an audience. Load on 'content marketing', 'blog strategy', 'content plan', 'SEO content'.
- `biz-seo` — SEO Specialist — Use when a site must be found through search. Load on 'SEO', 'search ranking', 'keywords', 'organic traffic', 'indexing'.
- `biz-social` — Social Media Manager — Use when a brand must show up and converse on social platforms. Load on 'social media', 'post this', 'community', 'social strategy'.
- `biz-email` — Email Marketer — Use when a list must be reached with relevant messages. Load on 'email marketing', 'newsletter', 'email campaign', 'drip sequence'.
- `biz-sales` — Sales Engineer — Use when a technical product must be sold to a technical buyer. Load on 'sales engineer', 'demo', 'technical sales', 'POC', 'solution selling'.
- `biz-account` — Account Manager — Use when existing customers must be kept and grown. Load on 'account management', 'renewal', 'upsell', 'customer relationship'.
- `biz-partnerships` — Partnerships Manager — Use when a relationship with another company must create value. Load on 'partnership', 'integration partner', 'reseller', 'business development'.
- `biz-customer-success` — Customer Success Manager — Use when customers must reach value and stay. Load on 'customer success', 'onboarding the customer', 'adoption', 'renewal risk'.
- `biz-support` — Support Engineer — Use when users need help and problems must be resolved. Load on 'support', 'help the user', 'ticket', 'troubleshooting for a customer'.
- `biz-community` — Community Manager — Use when a community must be built and kept healthy. Load on 'community', 'forum', 'discord', 'moderation', 'community building'.
- `biz-legal` — Legal Counsel — Use when legal risk in a product or contract must be assessed. Load on 'legal', 'contract', 'terms of service', 'compliance risk', 'liability'.
- `biz-finance` — Finance Analyst — Use when money must be modelled, tracked or explained. Load on 'finance', 'budget', 'forecast', 'unit economics', 'runway'.
- `biz-recruiting` — Technical Recruiter — Use when technical roles must be filled well. Load on 'recruiting', 'hiring', 'sourcing', 'interview process', 'job description'.
- `biz-operations` — Business Operations Analyst — Use when processes across a company must be made to work. Load on 'business operations', 'process improvement', 'ops', 'internal process'.
- `biz-brand` — Brand Manager — Use when a brand must be kept consistent and strong. Load on 'brand management', 'brand guidelines', 'brand voice', 'brand consistency'.

## creative (16)

- `creative-copywriter` — Copywriter — Use when words must persuade or inform. Load on 'copy', 'headline', 'landing page copy', 'ad copy', 'write this'.
- `creative-storyteller` — Storyteller — Use when a narrative must carry meaning or emotion. Load on 'story', 'narrative', 'tell this as a story', 'arc'.
- `creative-screenwriter` — Screenwriter — Use when a script for film or video must be written. Load on 'script', 'screenplay', 'scene', 'dialogue', 'video script'.
- `creative-naming` — Naming Specialist — Use when a product, company or feature needs a name. Load on 'naming', 'name ideas', 'brand name', 'what should we call this'.
- `creative-voice` — Voice & Tone Specialist — Use when a brand's way of speaking must be defined. Load on 'voice and tone', 'brand voice', 'tone of voice', 'how should we sound'.
- `creative-editor` — Editor — Use when a piece of writing must be made clear and strong. Load on 'edit this', 'proofread', 'tighten this', 'review my writing'.
- `creative-producer` — Content Producer — Use when content must be made, not just imagined. Load on 'produce this', 'content production', 'shoot this', 'make the content'.
- `creative-video` — Video Editor — Use when footage must become a finished video. Load on 'edit video', 'cut this', 'video editing', 'timeline', 'post production'.
- `creative-audio` — Audio Engineer — Use when sound must be recorded, mixed or cleaned. Load on 'audio', 'mix this', 'record sound', 'clean up audio', 'mastering'.
- `creative-music` — Music Composer — Use when music must be written for a purpose. Load on 'compose', 'music for this', 'soundtrack', 'score', 'jingle'.
- `creative-illustrator` — Illustrator — Use when imagery must be drawn or rendered by hand. Load on 'illustrate', 'draw this', 'illustration', 'art for this'.
- `creative-photographer` — Photographer — Use when a real image must be captured. Load on 'photograph', 'shoot this', 'product photo', 'headshot', 'photo brief'.
- `creative-motion` — Motion Designer — Use when graphics must move. Load on 'motion design', 'animate this', 'kinetic type', 'logo animation', 'motion graphics'.
- `creative-3d-artist` — 3D Artist — Use when a three-dimensional asset or scene must be made. Load on '3D model', '3D scene', 'Blender', 'render', 'shading'.
- `creative-art-director` — Art Director — Use when the visual direction of a project must be set and held. Load on 'art direction', 'visual direction', 'creative direction', 'look and feel'.
- `creative-packaging` — Packaging Designer — Use when a product must be designed for the shelf or the doorstep. Load on 'packaging', 'label design', 'box design', 'unboxing'.

## agent (16)

- `agent-architect` — Agent Architect — Use when an AI agent or multi-agent system must be designed. Load on 'design an agent', 'agent architecture', 'multi-agent', 'how should this agent work'.
- `agent-tool-designer` — Tool Designer — Use when an agent needs a tool, function or API surface. Load on 'tool for the agent', 'function spec', 'tool schema', 'what tools should it have'.
- `agent-memory-engineer` — Agent Memory Engineer — Use when an agent must remember across turns, sessions or tasks. Load on 'agent memory', 'long-term memory', 'context store', 'remember across sessions'.
- `agent-evaluator` — Agent Evaluator — Use when an agent's quality must be measured. Load on 'evaluate the agent', 'eval', 'benchmark the agent', 'is it getting better'.
- `agent-guardrail-engineer` — Guardrail Engineer — Use when an agent must be kept inside safe and acceptable behaviour. Load on 'guardrails', 'safety for the agent', 'limits', 'what it must never do'.
- `agent-cost-optimizer` — Agent Cost Optimizer — Use when an agent's token, latency or money cost must come down. Load on 'too expensive', 'token cost', 'latency', 'optimize the agent cost'.
- `agent-orchestrator-designer` — Orchestration Designer — Use when several agents must work together. Load on 'orchestrate', 'multi-agent workflow', 'who does what', 'agent pipeline'.
- `agent-prompt-engineer` — Prompt Engineer — Use when a model's instruction must be made reliable. Load on 'prompt', 'system prompt', 'instruct the model', 'why does it not follow'.
- `agent-context-engineer` — Context Engineer — Use when an agent's context window must be managed well. Load on 'context window', 'too much context', 'summarize the history', 'context budget'.
- `agent-handoff-designer` — Handoff Designer — Use when work must pass cleanly between agents or humans. Load on 'handoff', 'hand over to', 'escalate', 'pass this along'.
- `agent-observability-engineer` — Agent Observability Engineer — Use when an agent's behaviour must be seen while it runs. Load on 'agent logs', 'trace the agent', 'observability', 'why did it do that'.
- `agent-error-recovery` — Error Recovery Engineer — Use when an agent must survive partial failures. Load on 'recovery', 'retry logic', 'the agent got stuck', 'fail gracefully'.
- `agent-verification` — Agent Verifier — Use when an agent's output must be checked before it is trusted. Load on 'verify', 'check the agent output', 'is this correct', 'review before use'.
- `agent-runtime-engineer` — Agent Runtime Engineer — Use when the loop that runs an agent must be built. Load on 'agent loop', 'runtime', 'execution engine', 'build the agent runner'.
- `agent-deployer` — Agent Deployer — Use when an agent must go to production and stay healthy. Load on 'deploy the agent', 'ship it', 'production', 'roll out'.
- `agent-design-loop` — Agent Design Loop — Use when an agent must be iterated from idea to reliable behaviour. Load on 'improve the agent', 'iterate on the agent', 'make it better', 'design loop'.

## self (16)

- `self-journal` — Journaling Coach — Use when a person wants to reflect in writing. Load on 'journal', 'diary', 'reflect on my day', 'write about this'.
- `self-habits` — Habit Coach — Use when behaviour must change over time. Load on 'habit', 'routine', 'streak', 'I want to start doing', 'stop doing'.
- `self-learning` — Learning Coach — Use when a skill or subject must be learned. Load on 'learn this', 'study plan', 'how do I get good at', 'curriculum'.
- `self-inbox` — Inbox Manager — Use when messages must be triaged and emptied. Load on 'inbox', 'email', 'clear my inbox', 'triage messages'.
- `self-calendar` — Calendar Manager — Use when time and commitments must be scheduled. Load on 'calendar', 'schedule this', 'find a time', 'plan my week'.
- `self-tasks` — Task Manager — Use when work must be captured, prioritized and finished. Load on 'todo', 'task list', 'what should I do next', 'prioritize'.
- `self-notes` — Notes Engineer — Use when knowledge must be captured so it can be found again. Load on 'notes', 'second brain', 'note-taking', 'organize my notes'.
- `self-reading` — Reading Assistant — Use when a lot must be read and understood. Load on 'read this', 'summarize this book', 'what is this article about', 'help me read'.
- `self-writing` — Writing Coach — Use when a person wants to write better. Load on 'writing', 'help me write', 'improve my writing', 'draft this'.
- `self-finance` — Personal Finance Coach — Use when a person's money must be organized. Load on 'budget', 'personal finance', 'save money', 'debt', 'spending'.
- `self-health` — Health & Energy Coach — Use when sleep, energy or daily physical habits must improve. Load on 'sleep', 'energy', 'exercise habit', 'feel tired'.
- `self-focus` — Focus & Attention Coach — Use when attention is scattered and deep work is needed. Load on 'focus', 'distraction', 'deep work', 'I cannot concentrate'.
- `self-decisions` — Decision Coach — Use when a person faces a hard choice. Load on 'decision', 'should I', 'help me decide', 'pros and cons'.
- `self-goals` — Goal & Review Coach — Use when long-term aims must be set and tracked. Load on 'goals', 'quarterly review', 'annual review', 'what am I aiming at'.
- `self-admin` — Life Admin Assistant — Use when the paperwork of life must be handled. Load on 'admin', 'appointments', 'bills', 'paperwork', 'organize my life admin'.
- `self-systems` — Personal Systems Designer — Use when a person's routines and tools should work together. Load on 'personal system', 'my workflow', 'organize my life', 'set up a system'.

## sys (16)

- `sys-shell` — Shell & Terminal Expert — Use when the command line must be used well. Load on 'shell', 'bash', 'PowerShell', 'command line', 'terminal'.
- `sys-dotfiles` — Dotfiles Engineer — Use when a machine's configuration must be managed. Load on 'dotfiles', 'config files', 'my setup', 'portable environment'.
- `sys-backup` — Backup & Recovery Engineer — Use when data must be protected and restorable. Load on 'backup', 'restore', 'data loss', 'disaster recovery'.
- `sys-sync` — Sync & File Movement Engineer — Use when files must stay consistent across machines or services. Load on 'sync', 'rsync', 'cloud sync', 'move these files'.
- `sys-install` — Package & Install Engineer — Use when software must be installed, upgraded or removed cleanly. Load on 'install', 'upgrade this', 'uninstall', 'package manager'.
- `sys-drivers` — Drivers & Hardware Specialist — Use when hardware must be recognized or made to work. Load on 'driver', 'device not working', 'hardware', 'peripheral'.
- `sys-perf` — System Performance Tuner — Use when a machine is slow and must be made faster. Load on 'slow computer', 'performance', 'optimize the machine', 'it is lagging'.
- `sys-security` — Personal Security Hardener — Use when a personal machine or account must be made safer. Load on 'security', 'harden', '2FA', 'password manager', 'am I secure'.
- `sys-net` — Network & Connectivity Engineer — Use when connectivity, DNS or a home network must work. Load on 'network', 'wifi', 'dns', 'no internet', 'router'.
- `sys-virtualization` — Virtualization Engineer — Use when a VM, container or sandbox must be set up. Load on 'VM', 'virtual machine', 'container', 'sandbox', 'Docker'.
- `sys-monitoring` — Personal Monitoring Engineer — Use when a home lab or personal server must be watched. Load on 'monitoring', 'uptime', 'alert me', 'home server', 'logs'.
- `sys-automation` — Personal Automation Engineer — Use when a repeated computer task should run itself. Load on 'automate this', 'script it', 'cron', 'scheduled task', 'make it run itself'.
- `sys-storage` — Storage & Disk Engineer — Use when disk space or storage layout must be managed. Load on 'disk full', 'storage', 'partition', 'clean up space'.
- `sys-updates` — Update & Patch Manager — Use when system and software updates must be applied safely. Load on 'update', 'patch', 'upgrade the system', 'should I update'.
- `sys-troubleshoot` — System Troubleshooter — Use when a computer misbehaves and the cause is unknown. Load on 'not working', 'it broke', 'troubleshoot', 'diagnose this'.
- `sys-power` — Power & Battery Engineer — Use when a laptop's battery life or power must be improved. Load on 'battery', 'power usage', 'laptop drains', 'battery health'.

## game (16)

- `game-designer` — Game Designer — Use when a game's mechanics and feel must be designed. Load on 'game design', 'mechanics', 'core loop', 'game idea', 'how should this play'.
- `game-level-designer` — Level Designer — Use when a game's spaces and pacing must be built. Load on 'level design', 'map', 'layout', 'pacing', 'encounter design'.
- `game-gameplay-engineer` — Gameplay Engineer — Use when a game's moment-to-moment systems must be coded. Load on 'gameplay code', 'player controller', 'combat system', 'game logic'.
- `game-graphics` — Game Graphics Programmer — Use when a game's rendering must look right and run fast. Load on 'shaders', 'rendering', 'graphics programming', 'it looks wrong', 'frame rate'.
- `game-physics` — Game Physics Engineer — Use when movement, collision or simulation must behave. Load on 'physics', 'collision', 'rigidbody', 'it clips through', 'movement feels wrong'.
- `game-ai` — Game AI Engineer — Use when non-player characters must behave believably. Load on 'game AI', 'enemy behaviour', 'NPC', 'pathfinding', 'behaviour tree'.
- `game-audio` — Game Audio Designer — Use when a game's sound and music must be implemented. Load on 'game audio', 'sound design', 'music for the game', 'SFX'.
- `game-ui` — Game UI Designer — Use when a game's interface and HUD must be designed. Load on 'game UI', 'HUD', 'menus', 'inventory screen', 'game interface'.
- `game-narrative` — Game Narrative Designer — Use when a game's story and world must be written. Load on 'game story', 'narrative', 'worldbuilding', 'dialogue', 'lore'.
- `game-balance` — Game Balance Designer — Use when a game's difficulty, economy or meta must be tuned. Load on 'balance', 'difficulty', 'economy', 'it is too hard', 'too easy'.
- `game-qa` — Game QA Engineer — Use when a game must be tested for bugs and regressions. Load on 'game testing', 'QA', 'bug', 'it crashes', 'repro steps'.
- `game-producer` — Game Producer — Use when a game project must ship on time. Load on 'game production', 'milestone', 'scope', 'schedule', 'when will it ship'.
- `game-tools` — Game Tools Engineer — Use when a game team needs better tools. Load on 'game tools', 'editor tooling', 'level editor', 'pipeline tool', 'automate the workflow'.
- `game-optimization` — Game Performance Engineer — Use when a game must hit its frame budget. Load on 'frame rate', 'performance', 'optimize the game', 'stuttering', 'memory'.
- `game-release` — Game Release Manager — Use when a game must be launched and kept live. Load on 'release the game', 'launch', 'store page', 'patching', 'live ops'.
- `game-monetization` — Game Monetization Designer — Use when a game must earn revenue fairly. Load on 'monetization', 'pricing', 'in-app purchases', 'battle pass', 'how to make money'.

