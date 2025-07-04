# The Algorithmic Mirror: Auditing TikTok Recommender Systems for Personalization, Protection, and Profiling

## Project pitchers and facilitators:

- Filip Hossner (KInIT, filip.hossner@kinit.sk),
- Adrián Bindas (KInIT, adrian.bindas@kinit.sk)

## Participants

- Afina Krisdianatha (a_finavien@outlook.com)
- Aanila Tarannum (atarann@iu.edu)
- Jurij Smrke (jurij.smrke@mirovni-institut.si)
- Loizos Bitsikokos (lbitsiko@purdue.edu)

## Designer

- Elena Aversa (elena.aversa@polimi.it)


## Background and purposes

Social platforms face a crisis as they become riddled with disinformation, harmful narratives or inappropriate content, further the spread of propaganda and machine-generated content while the content moderation is being restricted and the behavior of recommender systems is opaque and (intentionally) obfuscated. The damaging behavior of recommender systems is difficult to overlook as it showcases bias and echo chambers, raises privacy concerns, and fails to adhere to legal obligations.

To accurately describe and examine the problematic interactions between user generated content and recommender systems, an efficient and representative analysis of the recommender behaviour is required. This can be facilitated by so-called algorithmic audits.

In general, algorithmic auditing is a process of dynamic black-box assessment of real-world (AI-based) software system behavior. Since social media recommender systems are black-boxes (we cannot analyze or influence their inner workings), audits must explore their properties behaviorally: user interactions with an algorithm are simulated (e.g., content visits), and observed responses (e.g., recommended videos) are examined for the presence of the audited phenomenon. Typically, bots or human agents are employed to simulate such user interactions.

This novel type of social media algorithm analysis is in line with  the Digital Services Act (DSA) Article 37, which requires Very Large Online Platforms (VLOPs) such as TikTok, YouTube, Instagram, Facebook, LinkedIn and Very Large Online Search Engine (VLOSE) like Google Search to undergo regular assessments by external auditors to evaluate their compliance with DSA regulations. Our analysis of DSA audit reports published in Q4 2024, revealed that TikTok is the only platform that received a “negative” appraisal regarding compliance with recommender system transparency requirements.

The goal of our project is to employ algorithmic auditing to assess how TikTok recommender systems protect minors, preserve non-profiling of sensitive characteristics or allow users to turn off personalization of their video feeds.

## Research Questions:

Auditing of the social platform can provide valuable information about the design and behavior of its recommender systems. Analysis of data gathered during the audit can reveal details about recommender “explore” and “exploit” phases and the effect of personalization on recommendations.

The following main research question will be answered as part of the summer school project: 

- Do the TikTok recommender systems fulfill obligations stated by the Digital Services Act?

More specifically, we will aim to address (some or all of) the following more specific research questions:
- Is a user choice to turn off personalization of recommended items actually working?
- Are minors protected from their profiling in advertisement systems?
- Are users’ sensitive and protected characteristics (e.g., health state) omitted when providing personalized recommendations?

## Situating the project

The behavior of recommender systems has wide ethical and legal implications. DSA defines obligations for very large online platforms related to 1) recommender system transparency and user choices in recommender systems (Articles 27 & 38 of the DSA), 2) ban of profiling minors in advertisement systems (Article 28), and 3) restrictions on advertisements based on sensitive personal data (Article 26) .

This project is also closely related to the EU-funded vera.ai project, in which novel tools for supporting media professionals in combating false information are developed. Moreover, it relates to AI-Auditology, a research project in which we aim to fundamentally change the oversight of social media AI algorithms by a novel paradigm of model-based algorithmic auditing.

This summer school project serves a noble purpose and will contribute to a positive societal impact on the online media environment. Currently, media regulators, NGOs,  or researchers have no real tool to quantitatively investigate whether big tech follows on their self-regulatory promises or adheres to relevant legislation on tackling recommender system biases, mitigating toxic content, or preventing misinformation spread. The findings and outcomes of this summer school project will help to advance the research and development in our long-term goal of algorithmic auditing becoming a powerful watchdog tool, fully in line with European values.

## Methods, data sets, and tools:

Methods and data sets:

This project has a mixed character, combining quantitative and qualitative methods.

Its implementation will consist of three main interconnected activities, which may be flexibly adjusted (also considering ideas and expertise of individual participants). Namely:

- Activity 1: Quantitative analyses of pre-collected data from our past/ongoing auditing studies focused on TikTok (see our [recent paper](https://arxiv.org/abs/2504.18140) accepted to SIGIR 2025 conference for details). With this activity, we aim to get initial insight into understanding how TikTok recommender systems work. This analysis can also reveal some interesting hypotheses that can be further evaluated by Activity 2.
- Activity 2: Manual and qualitative micro-audit with dedicated smartphones on TikTok, with the potential to extend to other social media platforms. With pre-created TikTok accounts, we will manually control several users with various characteristics (e.g., minors as an experimental group, and adults as a control group) and behavior patterns (e.g., different interests or using different types of interactions). The observed recommended videos or advertisements will be also manually evaluated (e.g., to identify how many times the advertisement matched the protected sensitive characteristics of simulated users). After the end of user simulation, this approach can be extended by downloading GDPR data (containing all information about users and their interactions) and further quantitatively analysed as in Activity 1.
- Activity 3: Since Activity 2 will require audit scenarios that will define profiles of simulated users (e.g., age, gender) and behavior (e.g., if content with this hashtag is recommended, watch it until the end, otherwise skip it). Applying various Social Science and Humanities (SSH) approaches for defining such user archetypes can contribute in having the micro-audit to be representative and reliable.

Data processing tools (Activity 1):

- Pandas: data manipulation, analysis, and transformation
- Jupyter Notebooks: interactive data exploration, visualization and documentation
- LLMs (Large Language Models): text analysis, information extraction and text understanding through prompt engineering
- Whisper: Automated transcription of audio and video data
- [RAWGraphs](https://www.rawgraphs.io/): free and open source tool for data visualization

Auditing tools (Activity 2 and 3):
- Smartphones with pre-installed TikTok application and pre-created TikTok accounts
- LLMs (Large Language Models): to determine representative user archetypes (profiles, behaviour) through prompt engineering
- TikTok feature to export GDPR data
- [Zeeschuimer](https://github.com/digitalmethodsinitiative/zeeschuimer): a browser extension that collects social media data

## Preliminary findings

Our previous replication study examining the TikTok platform has confirmed a high impact of personalisation factors, such as geographical location and passive watching on recommendations. The study has also shown low reproducibility and short-term validity of findings of previous audits.
Subsequent research on this topic, utilizing methods described above, can help examine and explain the behavior of the TikTok recommender system and improve the auditing platform.

## References

- [Holding Big Platforms Accountable: The Why, What, and How of Auditing](https://kinit.sk/holding-big-platforms-accountable-why-what-how-of-auditing/)
    - Our blog post about [DSA](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2065) obligations related to media algorithms and how algorithmic auditing can strengthen whether platforms fulfill them
- [Revisiting Algorithmic Audits of TikTok: Poor Reproducibility and Short-term Validity of Findings](https://arxiv.org/abs/2504.18140)
    - Our replication study of algorithmic audits of TikTok personalization factors. The data collected during this study may be used during the Activity 1 to obtain initial insight into TikTok recommender systems.
- [Model-based Algorithmic Auditing of Social Media AI Algorithms](https://drive.google.com/file/d/19Cc5bTmjJb3ejBsINIrEknx1Q8k_2OzH/view?usp=drive_link)
    - Our concept paper introducing a novel concept of model-based algorithmic auditing and how we aim to achieve it by research and development of AI-Auditology platform. It provides further details on algorithmic auditing and how manual audits (as one that will be conducted during the summer school) can be partially automated.
