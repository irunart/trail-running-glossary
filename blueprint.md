# Trail running i18n Encyclopedia - Blueprint

## Project Background
This project is a collaboration with [itra.run](https://itra.run) initiated during the process of translating trail running content into Chinese. It aims to evolve beyond a simple translation effort into a comprehensive, open-source multi-lingual trail glossary.

## Project Objectives
- **Go-to Resource:** Build the go-to resource for multi-language references related to trail running.
- **Community Reference:** Provide a reliable source of terms for the broader trail running community.
- **Standardization:** Help future translators, reviewers, and journalists use correct and well-perceived terms in their writing.
- **Multilingual Support:** Build and maintain a glossary that supports multiple languages, starting with the insights gained from the Chinese translation process.

## Target Audience
- ITRA website translators
- Trail running news reporters
- Sports science researchers
- Trail runners
- Reviewers and journalists

## Collaboration Model
- **Open Source:** Hosted on GitHub.
- **Editorial Process:** Utilize the GitHub issue tracker for updates and editorial gate-keeping.
- **Community Driven:** Open to contributions from the broader trail running community.

## Technical Format
- **Automation:** Content will be auto-compiled into different formats.
- **Primary Output:** Mainly web hosting for easy access and reference.

## Data Structure
We use a **Structured Markdown** approach to ensure it is human-readable and easy to edit via GitHub Web UI.

**File Location:** `glossary/<slug>.md` (e.g., `glossary/performance-index.md`)

**File Content Template:**
```markdown
# [English Term]

## Meta
- **Definition:** [The canonical definition/explanation of the term. This serves as the reference for all languages.]
- **Category:** [e.g., ITRA System, Gear, Medical]
- **Tags:** [comma, separated, tags]
- **Reference URL:** [Link to official doc] (sample)
- **Reference Sentence:** [Contextual usage sentence] (sample)

## English (EN)
- **Term:** [Term in English]
- **Status:** [Official | Reviewed | Draft]

## French (FR)
- **Term:** [Term in French]
- **Status:** [Official | Reviewed | Draft]

## Spanish (ES)
- **Term:** [Term in Spanish]
- **Status:** [Official | Reviewed | Draft]

## Chinese (ZH)
- **Term:** [Term in Chinese]
- **Status:** [Reviewed | Draft]
- **Notes:** [Optional specific context]
```



## Sample Terms
- **Performance Index (PI):** ITRA 表现分
    - *Explanation:* A number [1, 999] to describe a runner's overall capability by taking into consideration the top performing X races in the last X months. The PI is assigned for each individual race and aggregated across races to build the runner's PI.
- **Score:** ITRA 积分
    - *Explanation:* A number [1, 6] to describe the difficulty of a course. It considers multiple factors like distance, elevation again, checkpoint frequency, etc.

## Resources
- **ITRA official translation mappings:** A list of reserved keywords and official translations provided by the ITRA team.
- **Common trail running terms:**
    - [超跑笔记 (WeChat)](https://mp.weixin.qq.com/s/K8NZ8tmCslBRtgUdxRKGlQ) - a reference for common trail running terminology.
- **Sample Glossary (Reference):** [Google Doc](https://docs.google.com/document/d/1LNC_Y0eGw1hK7cdnMoHU3S4o48RlMFbeGcsZnk9L07A/edit?tab=t.0) - serves as a content reference and solid format reference for establishing the review process.


## Initial Contributors
1. Boyu Wang
2. Chuanhao Liu
3. Junyi Pang
4. Ke Zhang
5. Nongshen Zhou
6. Pili Hu
7. Sheng Qian
8. Songlu Wang
9. Wei Chen
10. Xinhao Zhang
11. Xu Liu
12. Yao Song


