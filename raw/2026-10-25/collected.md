# Collected: 2026-10-18 〜 2026-10-25

> scripts/collect.py の自動出力。/weekly コマンドの入力。

## 1. 標準リポジトリの動き

### AGWG / WCAG

- [w3c/wcag#4995](https://github.com/w3c/wcag/pull/4995) Clarifications to labels or instructions SC  
  merged · PR · @scottaohara · 💬4 · Understanding, 3.3.2 Labels or instructions, Substantive, Non-Normative
  > Closes #4977 This PR attempts to clarify expectations around when labels, instructions or both might be necessary for form fields / controls. Key changes: - expand the concepts introduced in the first paragraph of the current doc into multiple paragraphs in this revision - try to clarify that the example of radios/checkboxes labels and the labels for options within a select-only combobox are simil…
- [w3c/wcag#5413](https://github.com/w3c/wcag/pull/5413) Rename "Key Terms" to "Glossary" in understanding and add intro paragraph  
  opened · PR · @patrickhlauke · 💬6 · Understanding
  > Renames "Key Terms" to "Glossary" in understanding (to match the actual normative specification) and adds a bit of introductory context to the start of the disclosure widget. Hopefully this reinforces the idea that these are not just informative made-up things from understanding, but actual references to normative / specification definitions Closes https://github.com/w3c/wcag/issues/5409 Preview: …
- [w3c/wcag#5426](https://github.com/w3c/wcag/pull/5426) Fix i18n issues in relative-luminance.html  
  opened · PR · @remibetin · 💬2 · Editorial, Bug Fixes
  > This backports https://github.com/w3c/wcag/pull/3467 to the `WCAG-2.1` branch. The current lines are flagged by the [Internationalization Checker](https://validator.w3.org/i18n-checker/): See [report](https://validator.w3.org/i18n-checker/check?uri=https%3A%2F%2Fwww.w3.org%2FTR%2FWCAG21%2Frelative-luminance.html#validate-by-uri+). This recently created confusion with a lead translation organizatio…
- [w3c/wcag#5425](https://github.com/w3c/wcag/pull/5425) Update the base stylesheet used in relative-luminance.html  
  opened · PR · @remibetin · 💬2 · Bug Fixes
  > Note: I'm opening a draft pull request because adding the `.toc-inline` class to the body element feels like a workaround. Resolves https://github.com/w3c/wcag/issues/5424. Note: The change will also need to be backported to the `WCAG-2.1` branch.
- [w3c/wcag#5420](https://github.com/w3c/wcag/issues/5420) WCAG 2.2 JSON Duplicate Technique G101 in JSON  
  opened · Issue · @airbr · 💬2
  > In the officially published JSON for WCAG 2.2 there appears to be duplicate entries for a technique to Success Criteria 3.1.3 Unusual Words: EDIT: This may be confusion on my part. It may be a bug in my code. But the similarity somehow snagged my little application This is related to the Published Code as at this moment at https://www.w3.org/WAI/WCAG22/wcag.json <img width="1263" height="449" alt=…
- [w3c/wcag#5421](https://github.com/w3c/wcag/pull/5421) Tweak 1.4.1 Use of Color understanding note wording regarding contrast  
  opened · PR · @patrickhlauke · 💬1 · Understanding, 1.4.1 Use of Color, Substantive
  > Closes #5418 Preview: second note in https://deploy-preview-5421--wcag2.netlify.app/understanding/use-of-color#intent Diff: https://services.w3.org/htmldiff?doc1=https%3A%2F%2Fwww.w3.org%2FWAI%2FWCAG22%2FUnderstanding%2Fuse-of-color.html&doc2=https%3A%2F%2Fdeploy-preview-5421--wcag2.netlify.app%2Funderstanding%2Fuse-of-color#intent
- [w3c/wcag#5423](https://github.com/w3c/wcag/pull/5423) Bump markdown-it from 14.3.2 to 14.3.3  
  opened · PR · @dependabot[bot] · 💬1 · dependencies, javascript
  > Bumps [markdown-it](https://github.com/markdown-it/markdown-it) from 14.3.2 to 14.3.3. <details> <summary>Changelog</summary> <p><em>Sourced from <a href="https://github.com/markdown-it/markdown-it/blob/14.3.3/CHANGELOG.md">markdown-it's changelog</a>.</em></p> <blockquote> <h2>[14.3.3] - 2026-10-16</h2> <h3>Security</h3> <ul> <li>Backported 15.0.3 fixes.</li> </ul> </blockquote> </details> <detai…
- [w3c/wcag#5418](https://github.com/w3c/wcag/issues/5418) Clarification: Does SC 1.4.1 require colours to differ in hue, or can a sufficient lightness difference alone provide the additional visual distinction?  
  opened · Issue · @JoReavell · 💬1
  > ### Summary The note in the Understanding document for SC 1.4.1 appears to be causing inconsistent interpretations regarding whether colours must differ in hue in order to benefit from the exception relating to lightness differences. **Current wording:** "If content is conveyed through the use of colors that differ **not only in their hue, but that also have a significant difference in lightness**…
- [w3c/wcag#5424](https://github.com/w3c/wcag/issues/5424) Update the stylesheet used for relative-luminance.html  
  opened · Issue · @remibetin · 💬0 · Technical (bug)
  > The [relative-luminance.html](https://www.w3.org/TR/WCAG22/relative-luminance.html) page uses the following stylesheet: https://www.w3.org/StyleSheets/TR/base.css This stylesheet seems to be outdated: it was last updated in 2020. According to the [tr-design documentation](https://w3c.github.io/tr-design/src/README#using), the current stylesheet is located at https://www.w3.org/StyleSheets/TR/2021/…
- [w3c/wcag#5417](https://github.com/w3c/wcag/issues/5417) Section 5.5 Statement of Partial Conformance - Language is ... unclear  
  opened · Issue · @patrickhlauke · 💬0 · ErratumRaised, Conformance WCAG 2.x
  > The wording for https://www.w3.org/TR/WCAG22/#conformance-partial-lang took me a few times to understand. It seems that, in practice, this refers particularly to cases like "The site is in human language X (say 'Swiss German'), but there's no screen reader support for that language". I struggle to think of any other scenarios where the human language of content could lead to the inability to satis…
- [w3c/wcag#5373](https://github.com/w3c/wcag/issues/5373) Conforming Alternate Version (CAV) and the mechanism to reach/achieve it  
  closed · Issue · @patrickhlauke · 💬21 · 3.3.2 Labels or instructions, Conformance WCAG 2.x, 2.4.6 Headings and Labels, Response-Only
- [w3c/wcag#4977](https://github.com/w3c/wcag/issues/4977) Consider providing examples of when controls _don't_ need labels - 3.3.2 labels or instructions  
  closed · Issue · @scottaohara · 💬9 · Understanding, 3.3.2 Labels or instructions
- [w3c/wcag#5287](https://github.com/w3c/wcag/pull/5287) Update Statement of Partial Conformance  
  closed · PR · @bruce-usab · 💬6 · ErratumRaised, Conformance WCAG 2.x
- [w3c/wcag#5414](https://github.com/w3c/wcag/pull/5414) Add styles to open details/summary disclosures when printing  
  closed · PR · @patrickhlauke · 💬5 · Technical (bug)
- [w3c/wcag#5422](https://github.com/w3c/wcag/pull/5422) Update use-of-color.html  
  closed · PR · @vladyslav20082008-bot · 💬1
- [w3c/wcag#5419](https://github.com/w3c/wcag/issues/5419) Hello, I have a question regarding the appropriate use of aria-current in a specific UX scenario.  
  closed · Issue · @domenicogirolamo6-eng · 💬0
- [w3c/wcag#5415](https://github.com/w3c/wcag/issues/5415) Homegrown partial conformance  
  closed · Issue · @kreukelzone · 💬0
- [w3c/wcag#799](https://github.com/w3c/wcag/issues/799) Screen, Display, Reflow, Adaptive and Responsive  
  updated · Issue · @jake-abma · 💬21 · Understanding, 1.3.4 Orientation
- [w3c/wcag#5305](https://github.com/w3c/wcag/pull/5305) Add G227: Using the Map Equivalent Purpose Framework for digital geographic maps  
  updated · PR · @frastlin · 💬18 · Techniques, 1.1.1 Non-text content, Substantive
- [w3c/wcag#4717](https://github.com/w3c/wcag/issues/4717) Is iOS's three finger zoom defined as "assistive technology" on native mobile apps?  
  updated · Issue · @kylenowcrylater · 💬18 · Public Comment, Response-Only
- [w3c/wcag#5409](https://github.com/w3c/wcag/issues/5409) In Understanding, replace heading “Key Terms” with “Relevant Glossary Entries” or similar  
  updated · Issue · @yatil · 💬10
- [w3c/wcag#5263](https://github.com/w3c/wcag/issues/5263) Section 5.4 Third Party Content is missnamed  
  updated · Issue · @bruce-usab · 💬6 · ErratumRaised, Conformance WCAG 2.x
- [w3c/wcag#5192](https://github.com/w3c/wcag/pull/5192) Update F74.html  
  updated · PR · @detlevhfischer · 💬5 · Techniques, 1.2.8 Media Alternative, 1.2.2 Captions (Prerecorded)
- [w3c/wcag#2532](https://github.com/w3c/wcag/pull/2532) Update 3.3.2 Labels or Instructions understanding - add requirement for permanently available labels  
  updated · PR · @detlevhfischer · 💬4 · Understanding, 3.3.2 Labels or instructions, Substantive
- [w3c/wcag#5407](https://github.com/w3c/wcag/pull/5407) Change "correct" to "appropriate" in 4.1.2 "in brief"  
  updated · PR · @patrickhlauke · 💬4 · Understanding, 4.1.2 Name Role Value
- [w3c/wcag#5396](https://github.com/w3c/wcag/pull/5396) Add map and third party guidance to Understanding 1.4.11  
  updated · PR · @jsabutis · 💬3
- [w3c/wcag#5228](https://github.com/w3c/wcag/pull/5228) Add new examples and resource link to Understanding Three Flashes or Below Threshold  
  updated · PR · @thealexmosk · 💬3
- [w3c/wcag#5362](https://github.com/w3c/wcag/pull/5362) Update 1.4.11 Non-text Contrast with additional boundary examples  
  updated · PR · @Blackbaud-MattGregg · 💬3 · 1.4.11 Non-text contrast
- [w3c/wcag#2217](https://github.com/w3c/wcag/issues/2217) 6. Glossary: EDIT Image of Text Definition  
  updated · Issue · @BridgesHelpdesk · 💬3 · WCAG 2.0, 1.2: Time-based Media, 1.4.5 Images of text
- [w3c/wcag#4975](https://github.com/w3c/wcag/pull/4975) Update H91  
  updated · PR · @goetsu · 💬3 · Techniques
- [w3c/wcag#5375](https://github.com/w3c/wcag/pull/5375) Update error identification to add reference to 1.3.1 and remove some links to ARIA techniques  
  updated · PR · @fstrr · 💬3 · Techniques, Understanding, 1.3.1 Info and Relationships
- [w3c/wcag#5403](https://github.com/w3c/wcag/pull/5403) Tweak "programmatically determined" definition example  
  updated · PR · @patrickhlauke · 💬2 · ErratumRaised, Normative
- [w3c/wcag#5124](https://github.com/w3c/wcag/issues/5124) Proposal: New General Technique for SC 1.1.1, using the Map Equivalent Purpose (MEP) Framework for digital geographic maps  
  updated · Issue · @frastlin · 💬1
- [w3c/wcag#5411](https://github.com/w3c/wcag/pull/5411) non-text-contrast: add clarification on button indication, fix typo  
  updated · PR · @fstrr · 💬1 · 1.4.11 Non-text contrast
- [w3c/wcag#4771](https://github.com/w3c/wcag/pull/4771) New Failure Technique for 1.4.13 Content on hover or focus when the pointer cannot be moved over the new popup content without that content closing  
  updated · PR · @detlevhfischer · 💬1 · Techniques, Understanding, 1.4.13 Content on Hover or Focus, Substantive
- [w3c/wcag#5386](https://github.com/w3c/wcag/pull/5386) Expand F13: add example image, expand the explanation and test procedure, make it a 1.3.3 failure as well  
  updated · PR · @patrickhlauke · 💬1 · Techniques, Substantive
- [w3c/wcag#5400](https://github.com/w3c/wcag/issues/5400) [spam]  
  updated · Issue · @umahr086-dot · 💬0
- [w3c/wcag3#939](https://github.com/w3c/wcag3/pull/939) Update reporting tier definitions and structure  
  opened · PR · @alastc · 💬1
  > Based on the review of the definitions: https://docs.google.com/presentation/d/1-Tglj2i-2VXbeqcxi8pHS872JB05zYFCUPzDfYe6z6M/edit?slide=id.h2597c101ee1c2d72_0_0#slide=id.h2597c101ee1c2d72_0_0 and minutes: https://www.w3.org/2026/10/20-ag-minutes.html#19d0
- [w3c/wcag3#938](https://github.com/w3c/wcag3/pull/938) Place permalinks after headings (fixes #868)  
  opened · PR · @philorien · 💬1
  > Guideline (`h4`) and provision (`h5`) permalinks were inserted before their headings, while ReSpec-generated sections place them after. This makes the reading order consistent, with the permalink following the heading, as requested in #868. Verified in the dev server: all 336 section permalinks follow their heading, and the visual position is unchanged (the links are absolutely positioned). Not te…
- [w3c/wcag3#926](https://github.com/w3c/wcag3/pull/926) Update biometrics provisions  
  opened · PR · @fstrr · 💬1
  > closes #572 1. updates Biometrics Not Relied Upon provision 2. Removes Multiple Biometrics Available and Voice Identification Not Relied Upon provisions.
- [w3c/wcag3#941](https://github.com/w3c/wcag3/issues/941) WCAG 3 WD (Sept 2026) - experience report: rendering the draft's outcomes over real WCAG 2.2 findings  
  opened · Issue · @kinti · 💬0
  > Hello, I maintain an open-source WCAG 2.2 auditing engine (a11y-toolkit, MIT, 32 MCP tools) that also powers a small production accessibility service. After the September 2026 Working Draft, we shipped a preview tool that takes a regular WCAG 2.2 audit report from a real site and re-groups its findings under the draft's 46 outcomes, with the draft's exact outcome names. It deliberately produces no…
- [w3c/wcag3#940](https://github.com/w3c/wcag3/issues/940) Explore the notion of accurate and important for the core requirement of Non-text content not relied on  
  opened · Issue · @mbgower · 💬0
  > If there is any part of WCAG 2 that has been a demonstrable failure, it is the lack of improvement on 1.1.1 Non-Text Content. The web is full of articles on how people should write text equivalents, yet in the situations where alternative text _exists_, it is incredibly non-uniform, and often not as useful as it could be. I have an existing proposal I respectfully request the people involved in No…
- [w3c/wcag3#924](https://github.com/w3c/wcag3/issues/924) Reference implementation portability and test vectors for the contrast algorithm  
  opened · Issue · @sbustelo · 💬0
  > The current contrast algorithm has a reference implementation in JavaScript (apca-w3), but no language-independent test vectors. If the algorithm becomes normative in WCAG 3, implementers in other languages (Python, PHP, C#, etc.) will port it manually, and there is no mechanism to verify that the ports produce identical results. This is not a new problem: #225 raised it for constant naming, and #…
- [w3c/wcag3#931](https://github.com/w3c/wcag3/issues/931) COGA support for interactive element importance indicated  
  opened · Issue · @lseeman · 💬0 · coga, Path: Input and focus⹁ interactive components, P - Interactive element importance indicated
  > We like this exploratory provision and would like to see it move forward. Please let us know if we can help. For example, if you have a specific research question, we can ask our members for life experience or subject matter expertise. We could also try to do a literary review or see what research is out there if that is more helpful. All the best, The COGA task force
- [w3c/wcag3#937](https://github.com/w3c/wcag3/issues/937) COGA support for copying supported  
  opened · Issue · @lseeman · 💬0 · coga, P - Copying supported
  > We really like this exploratory provision and would like to see it move forward. Please let us know if we can help. For example, if you have a specific research question, we can ask our members for life experience or subject matter expertise. We could also try to do a literary review or see what research is out there if that is more helpful. All the best, The COGA task force
- [w3c/wcag3#936](https://github.com/w3c/wcag3/issues/936) COGA support for no artificial time limits  
  opened · Issue · @lseeman · 💬0 · coga, P - No artificial time limits
  > We really like this exploratory provision and would like to see it move forward. Please let us know if we can help. For example, if you have a specific research question, we can ask our members for life experience or subject matter expertise. We could also try to do a literary review or see what research is out there if that is more helpful. All the best, The COGA task force
- [w3c/wcag3#935](https://github.com/w3c/wcag3/issues/935) COGA support for "Single flash"  
  opened · Issue · @julierawe · 💬0 · coga, P - Single flash
  > Hi, We really like this exploratory provision ("[Single flash](https://w3c.github.io/wcag3/guidelines/#single-flash)") and would like to see it move forward. Please let us know if we can help. For example, if you have a specific research question, we can ask our members for life experience or subject matter expertise. All the best, The COGA task force
- [w3c/wcag3#934](https://github.com/w3c/wcag3/issues/934) COGA support for "Non-verbal cues identified in transcripts"  
  opened · Issue · @julierawe · 💬0 · coga, P - Non-verbal cues identified in transcripts
  > Hi, We really like this exploratory provision ("[Non-verbal cues identified in transcripts](https://w3c.github.io/wcag3/guidelines/#non-verbal-cues-identified-in-transcripts)") and would like to see it move forward. Please let us know if we can help. For example, if you have a specific research question, we can ask our members for life experience or subject matter expertise. All the best, The COGA…
- [w3c/wcag3#933](https://github.com/w3c/wcag3/issues/933) COGA support for interactive elements distinguishable  
  opened · Issue · @lseeman · 💬0 · coga, P - Interactive elements distinguishable
  > We really like this exploratory provision on interactive elements distinguishable. It is very important and would like to see it move forward. Please let us know if we can help. For example, if you have a specific research question, we can ask our members for life experience or subject matter expertise. We could also try to do a literary review or see what research is out there if that is more hel…
- [w3c/wcag3#932](https://github.com/w3c/wcag3/issues/932) COGA support for "Figure captions persistent"  
  opened · Issue · @julierawe · 💬0 · coga, P - Figure captions persistent
  > Hi, We really like this exploratory provision ("[Figure captions persistent](https://w3c.github.io/wcag3/guidelines/#figure-captions-persistent)") and would like to see it move forward. Please let us know if we can help. For example, if you have a specific research question, we can ask our members for life experience or subject matter expertise. All the best, The COGA task force
- [w3c/wcag3#930](https://github.com/w3c/wcag3/issues/930) COGA support for "Captions consistent"  
  opened · Issue · @julierawe · 💬0 · coga, P - Captions consistent
  > Hi, We really like this exploratory provision ("[Captions consistent](https://w3c.github.io/wcag3/guidelines/#captions-consistent)") and would like to see it move forward. Please let us know if we can help. For example, if you have a specific research question, we can ask our members for life experience or subject matter expertise. All the best, The COGA task force
- [w3c/wcag3#929](https://github.com/w3c/wcag3/issues/929) COGA support for numerical alternatives available  
  opened · Issue · @lseeman · 💬0 · coga, P - Numerical alternatives available
  > We really need something like this exploratory provision on numerical alternatives available and would like to see it move forward (assuming other issues are addressed). Please let us know if we can help. For example, if you have a specific research question, we can ask our members for life experience or subject matter expertise. We could also try to do a literary review or see what research is ou…
- [w3c/wcag3#928](https://github.com/w3c/wcag3/issues/928) COGA support for non-verbal cues identified in captions  
  opened · Issue · @lseeman · 💬0 · coga, P - Non-verbal cues identified in captions
  > We really like this exploratory provision for non-verbal cues identified in captions and would like to see it move forward. Please let us know if we can help. For example, if you have a specific research question, we can ask our members for life experience or subject matter expertise. We could also try to do a literary review or see what research is out there if that is more helpful. All the best,…
- [w3c/wcag3#927](https://github.com/w3c/wcag3/issues/927) COGA support for "Non-verbal cues identified in audio descriptions"  
  opened · Issue · @julierawe · 💬0 · coga, P - Non-verbal cues identified in audio desc
  > Hi, We really like the exploratory provision "[Non-verbal cues identified in audio descriptions](https://w3c.github.io/wcag3/guidelines/#non-verbal-cues-identified-in-audio-descriptions)" and would like to see it move forward. Please let us know if we can help. For example, if you have a specific research question, we can ask our members for life experience or subject matter expertise. All the bes…
- [w3c/wcag3#925](https://github.com/w3c/wcag3/issues/925) "Media alternatives controllable" is redundant  
  opened · Issue · @mitchellevan · 💬0 · P - Captions controllable, P - Media alternatives controllable, P - Audio descriptions controllable
  > ### Currently "Media alternatives controllable" is redundant to "Captions controllable" and "Audio descriptions controllable". [Captions controllable](https://w3c.github.io/wcag3/guidelines/#captions-controllable): > A mechanism is available to turn captions on and off. > > Except when captions are hard-coded into the video content. [Audio descriptions controllable](https://w3c.github.io/wcag3/gui…
- [w3c/wcag3#221](https://github.com/w3c/wcag3/issues/221) Too much contrast: halation, overstimulation, and the APCA  
  updated · Issue · @Seirdy · 💬14 · Type: research, Path: Single sense and contrast
- [w3c/wcag3#505](https://github.com/w3c/wcag3/issues/505) Should bidirectional navigation be symmetrical?  
  updated · Issue · @fstrr · 💬13 · Path: Input and focus⹁ interactive components, P - Bidirectional navigation
- [w3c/wcag3#744](https://github.com/w3c/wcag3/issues/744) Update the definition of text  
  updated · Issue · @alastc · 💬9 · Path: Text and wording, Other: Definitions & Terminology, P - Text contrast sufficient (minimum), P - Text detectable
- [w3c/wcag3#533](https://github.com/w3c/wcag3/issues/533) why say human languages?  
  updated · Issue · @sydneycolemanfromgoogle · 💬9 · i18n, Path: Text and wording, Other: Definitions & Terminology, P - Common words used, P - Diacritics available
- [w3c/wcag3#702](https://github.com/w3c/wcag3/pull/702) update definition of Interactive Element  
  updated · PR · @fstrr · 💬6
- [w3c/wcag3#799](https://github.com/w3c/wcag3/pull/799) chore: use built-in cSpell HTML regex  
  updated · PR · @nschonni · 💬4
- [w3c/wcag3#914](https://github.com/w3c/wcag3/issues/914) WCAG 3: Functional Performance Statements  
  updated · Issue · @maryjom · 💬4
- [w3c/wcag3#834](https://github.com/w3c/wcag3/pull/834) Incorporate pre-CFC conformance section feedback  
  updated · PR · @adampage · 💬4
- [w3c/wcag3#902](https://github.com/w3c/wcag3/pull/902) Move accessibility supported to a new testing section and recast it as user agent supported  
  updated · PR · @mcking65 · 💬3
- [w3c/wcag3#543](https://github.com/w3c/wcag3/issues/543) Consider adding blurred content to Guideline 2.6.1 Avoid physical harm  
  updated · Issue · @mraccess77 · 💬3 · Path: User control and prevent harm
- [w3c/wcag3#572](https://github.com/w3c/wcag3/issues/572) Biometrics overlap  
  updated · Issue · @alastc · 💬3 · Path: Input and focus⹁ interactive components, P - Biometrics not relied on, P - Multiple biometrics available, P - Voice identification not relied on
- [w3c/wcag3#864](https://github.com/w3c/wcag3/pull/864) Update conformance section in Explainer  
  updated · PR · @tamsinewing555 · 💬3
- [w3c/wcag3#820](https://github.com/w3c/wcag3/issues/820) Input method versus input modality  
  updated · Issue · @adampage · 💬2 · Path: Input and focus⹁ interactive components, Other: Definitions & Terminology, P - Input method flexible
- [w3c/wcag3#923](https://github.com/w3c/wcag3/pull/923) Refactors glossary to use headings instead of definition list  
  updated · PR · @adampage · 💬2
- [w3c/wcag3#880](https://github.com/w3c/wcag3/pull/880) Scoping statement update  
  updated · PR · @alastc · 💬2 · Other: Introduction
- [w3c/wcag3#249](https://github.com/w3c/wcag3/issues/249) WCAG 3.0 Draft Review: Tradeoffs using flexible conformance  
  updated · Issue · @maryjom · 💬1 · Conformance
- [w3c/wcag3#868](https://github.com/w3c/wcag3/issues/868) Inconsistent reading order of headings and permalinks in guidelines doc  
  updated · Issue · @mcking65 · 💬1 · Other: Guideline Approach
- [w3c/wcag3#907](https://github.com/w3c/wcag3/pull/907) Add three exploratory sign language provisions  
  updated · PR · @iadawn · 💬1
- [w3c/wcag3#870](https://github.com/w3c/wcag3/issues/870) Use headings instead of definition list to structure the glossary  
  updated · Issue · @mcking65 · 💬1 · Other: Guideline Approach
- [w3c/wcag3#913](https://github.com/w3c/wcag3/issues/913) There should be no exception on Flashing  
  updated · Issue · @GreggVan · 💬1
- [w3c/wcag3#539](https://github.com/w3c/wcag3/issues/539) Keyboard interface input - Bidirectional navigation  
  updated · Issue · @sydneycolemanfromgoogle · 💬1 · Path: Input and focus⹁ interactive components, P - Bidirectional navigation
- [w3c/wcag2ict#1004](https://github.com/w3c/wcag2ict/pull/1004) Editorial issues arising from AG WG review of AAA content  
  merged · PR · @pday1 · 💬1 · Editorial
  > Minor editorial issues picked up by Mary Jo, Bruce and others. See commits for details.
- [w3c/wcag2ict#1005](https://github.com/w3c/wcag2ict/issues/1005) non-web documents AND/OR non-web software  
  opened · Issue · @GreggVan · 💬0
  > Pursuant to our meeting today when we noted that we sometimes use AND and sometimes use OR for non-web documents AND/OR non-web software I asked Claude Fable > in this document https://w3c.github.io/wcag2ict/ we use "non-web documents and non-web software" with an "and" in some places and an "or" in others. tell me how many times we use them as each (and or or) and where we use them. Titles, Notes…
- [act-rules/act-rules.github.io#2466](https://github.com/act-rules/act-rules.github.io/pull/2466) Update role-required-states-and-properties per ARIA 1.3  
  opened · PR · @shunguoy · 💬2 · Rule, WAI-ARIA 1.3
  > << Describe the changes >> Closes issue(s): - closes #2440 Need for Call for Review: This will require a 2 weeks Call for Review << new rule, or substantial changes affecting a large number of examples, if in doubt, use this. --- ## Pull Request Etiquette ### **When creating PR:** - [x] Make sure you're requesting to **pull a branch** (right side) to the `develop` branch (left side). - [x] Make su…
- [act-rules/act-rules.github.io#2464](https://github.com/act-rules/act-rules.github.io/pull/2464) Bump follow-redirects from 1.16.0 to 1.16.1  
  opened · PR · @dependabot[bot] · 💬1 · dependencies, javascript
  > Bumps [follow-redirects](https://github.com/follow-redirects/follow-redirects) from 1.16.0 to 1.16.1. <details> <summary>Commits</summary> <ul> <li><a href="https://github.com/follow-redirects/follow-redirects/commit/46301256333c90b7faac7aa126effe72ec16d16e"><code>4630125</code></a> Release version 1.16.1 of the npm package.</li> <li><a href="https://github.com/follow-redirects/follow-redirects/co…
- [act-rules/act-rules.github.io#2469](https://github.com/act-rules/act-rules.github.io/issues/2469) d  
  opened · Issue · @uhuh18153-tech · 💬0
  > Please describe the issue with references and relevant examples where necessary. --- or --- If authoring a proposal for a new rule, choose from one of the issue templates: - [Atomic Rule Template](https://raw.githubusercontent.com/act-rules/act-rules.github.io/develop/pages/design/atomic-template-empty.md) - [Composite Rule Template](https://raw.githubusercontent.com/act-rules/act-rules.github.io/…
- [act-rules/act-rules.github.io#2468](https://github.com/act-rules/act-rules.github.io/issues/2468) d  
  opened · Issue · @uhuh18153-tech · 💬0 · accessibility support
  > ## Accessibility support (( Put the accessibility support item here )) ## ACT Rules - ... List the rules here, link to its acc support section ## Examples ### Example 1 ... (( Add example here )) ```html code snippet here ``` [Open this example]() (( Add a link to a code pen or other hosted example. Keep in mind this example needs to be accessible and persistent. )) #### Preconditions Before runni…
- [act-rules/act-rules.github.io#2467](https://github.com/act-rules/act-rules.github.io/issues/2467) [0va7u6]  
  opened · Issue · @uhuh18153-tech · 💬0
  > +97430963985### ###
- [act-rules/act-rules.github.io#2465](https://github.com/act-rules/act-rules.github.io/issues/2465) Ediferia  
  closed · Issue · @itzaguerileon-star · 💬1 · accessibility support
- [act-rules/act-rules.github.io#2450](https://github.com/act-rules/act-rules.github.io/pull/2450) [rule]update to Aria 1.3: ARIA allowed accessibility child roles  
  updated · PR · @shunguoy · 💬1 · WAI-ARIA 1.3

### ARIA WG

- [w3c/aria#2928](https://github.com/w3c/aria/pull/2928) Chore: Enable stricter tooling -- enable respec validator and some specprod validators  
  merged · PR · @daniel-montalvo · 💬3
  > 🚀 **Netlify Preview**: 🔄 **this PR updates the following specs**: - [dpub-aria preview](https://deploy-preview-2928--wai-aria.netlify.app/dpub-aria/index.html) &mdash; [dpub-aria diff](https://services.w3.org/htmldiff?doc1=https%3A%2F%2Fw3c.github.io%2Fdpub-aria%2F&doc2=https%3A%2F%2Fdeploy-preview-2928--wai-aria.netlify.app%2Fdpub-aria%2Findex.html) This adds validators to catch some author error…
- [w3c/aria#2949](https://github.com/w3c/aria/pull/2949) Editorial: Aria 1.2 notes cleanup  
  merged · PR · @daniel-montalvo · 💬2 · editorial, spec:aria
  > 🚀 **Netlify Preview**: 🔄 **this PR updates the following specs**: - [ARIA preview](https://deploy-preview-2949--wai-aria.netlify.app/index.html) &mdash; [ARIA diff](https://services.w3.org/htmldiff?doc1=https%3A%2F%2Fw3c.github.io%2Faria%2F&doc2=https%3A%2F%2Fdeploy-preview-2949--wai-aria.netlify.app%2Findex.html) Closes #2809
- [w3c/aria#2951](https://github.com/w3c/aria/pull/2951) feat: add listview role to ARIA  
  opened · PR · @smhigley · 💬2 · spec:aria
  > 🚀 **Netlify Preview**: 🔄 **this PR updates the following specs**: - [ARIA preview](https://deploy-preview-2951--wai-aria.netlify.app/index.html) &mdash; [ARIA diff](https://services.w3.org/htmldiff?doc1=https%3A%2F%2Fw3c.github.io%2Faria%2F&doc2=https%3A%2F%2Fdeploy-preview-2951--wai-aria.netlify.app%2Findex.html) Closes #2036 Adds a listview role to the ARIA spec to support the interactive list p…
- [w3c/aria#2950](https://github.com/w3c/aria/pull/2950) Addition: fix the long-standing gap of how th scope=rowgroup should be mapped to align with HTML semantics  
  opened · PR · @scottaohara · 💬2 · spec:html-aam
  > 🚀 **Netlify Preview**: 🔄 **this PR updates the following specs**: - [html-aam preview](https://deploy-preview-2950--wai-aria.netlify.app/html-aam/index.html) &mdash; [html-aam diff](https://services.w3.org/htmldiff?doc1=https%3A%2F%2Fw3c.github.io%2Fhtml-aam%2F&doc2=https%3A%2F%2Fdeploy-preview-2950--wai-aria.netlify.app%2Fhtml-aam%2Findex.html)
- [w3c/aria#2948](https://github.com/w3c/aria/pull/2948) Editorial: clarify sync'd notes in main, banner and contentinfo  
  opened · PR · @scottaohara · 💬2 · editorial, spec:aria
  > 🚀 **Netlify Preview**: 🔄 **this PR updates the following specs**: - [ARIA preview](https://deploy-preview-2948--wai-aria.netlify.app/index.html) &mdash; [ARIA diff](https://services.w3.org/htmldiff?doc1=https%3A%2F%2Fw3c.github.io%2Faria%2F&doc2=https%3A%2F%2Fdeploy-preview-2948--wai-aria.netlify.app%2Findex.html) This is an editorial update from the work that was done in PR https://github.com/w3c…
- [w3c/aria#2947](https://github.com/w3c/aria/pull/2947) Chore: Process updates  
  opened · PR · @daniel-montalvo · 💬2
  > Proposed updates to the ARIA Process in prep for adopting an "evergreen" approach. You can select the rich diff on the PR files changed tab or read through following this [preview](https://github.com/w3c/aria/blob/process-updates/documentation/process.md)
- [w3c/aria#2809](https://github.com/w3c/aria/issues/2809) Editorial notes on combo box and more globally around 1.2-- should remove or edit  
  closed · Issue · @daniel-montalvo · 💬0 · ARIA 1.3
- [w3c/aria#2181](https://github.com/w3c/aria/pull/2181) Expectations for aria-hidden and focused elements  
  updated · PR · @scottaohara · 💬37 · Agenda, spec:aria
- [w3c/aria#2841](https://github.com/w3c/aria/issues/2841) Filtering a listbox with a text field (filterable select)  
  updated · Issue · @josepharhar · 💬14 · F2F
- [w3c/aria#2036](https://github.com/w3c/aria/issues/2036) Interactive Lists  
  updated · Issue · @MarioBatusic · 💬12 · F2F, feature
- [w3c/aria#2569](https://github.com/w3c/aria/issues/2569) "the age old question about whether a label should override content"  
  updated · Issue · @pkra · 💬9 · F2FCandidate
- [w3c/aria#2929](https://github.com/w3c/aria/pull/2929) clarification: text nodes and allowed accessibility child roles  
  updated · PR · @pkra · 💬6 · clarification, spec:aria, needs ACT review
- [w3c/aria#2623](https://github.com/w3c/aria/issues/2623) Discussion: Should AccName split name/label from contents (descendent text node contents)?  
  updated · Issue · @cookiecrook · 💬6 · F2F
- [w3c/aria#2748](https://github.com/w3c/aria/issues/2748) gathering ideas for browser dev tools improvements and what to do about them  
  updated · Issue · @pkra · 💬5 · F2F, deep-dive
- [w3c/aria#2914](https://github.com/w3c/aria/pull/2914) Editorial: Security considerations (from 2869)  
  updated · PR · @daniel-montalvo · 💬4 · spec:aria
- [w3c/aria#2818](https://github.com/w3c/aria/pull/2818) Add mappings for CSS display property.  
  updated · PR · @jcsteh · 💬4 · spec:css-aam
- [w3c/aria#2782](https://github.com/w3c/aria/issues/2782) Draft menu-element accessibility proposal  
  updated · Issue · @davidsgrogan · 💬4 · F2F
- [w3c/aria#2876](https://github.com/w3c/aria/issues/2876) Intro to using AI tools for ARIA contributors  
  updated · Issue · @jnurthen · 💬3 · F2F
- [w3c/aria#2883](https://github.com/w3c/aria/issues/2883) aria-actions on a non-focusable ancestor behavior on descendants is undefined  
  updated · Issue · @cookiecrook · 💬3 · F2F
- [w3c/aria#2922](https://github.com/w3c/aria/issues/2922) Advancing ARIA IDL  
  updated · Issue · @rahimabdi · 💬3 · F2FCandidate
- [w3c/aria#2903](https://github.com/w3c/aria/issues/2903) F2F: WPT Accessibility Updates Session in the ARIA WG TPAC schedule  
  updated · Issue · @cookiecrook · 💬2 · F2F
- [w3c/aria#2804](https://github.com/w3c/aria/pull/2804) html-aam: map new menu html elements to aria roles  
  updated · PR · @davidsgrogan · 💬2 · spec:html-aam
- [w3c/aria#2920](https://github.com/w3c/aria/issues/2920) From WHATWG: a11y concerns around removing the blur event on element removal  
  updated · Issue · @davidsgrogan · 💬2 · F2F
- [w3c/aria#2916](https://github.com/w3c/aria/issues/2916) What should "supported" be in ACD?  
  updated · Issue · @lolaodelola · 💬2 · F2F
- [w3c/aria#2921](https://github.com/w3c/aria/issues/2921) From CSSWG: proposal to set ARIA attributes *on pseudo-elements only* via CSS  
  updated · Issue · @davidsgrogan · 💬2 · F2F
- [w3c/aria#2940](https://github.com/w3c/aria/issues/2940) Explore (and potentially improve) respec wpt test implementation  
  updated · Issue · @daniel-montalvo · 💬1
- [w3c/aria#2886](https://github.com/w3c/aria/issues/2886) WG process updates to combine "evergreen approach" with wide and AC review  
  updated · Issue · @daniel-montalvo · 💬1 · F2F
- [w3c/aria#2891](https://github.com/w3c/aria/issues/2891) accessibility approach for two-phase view transitions  
  updated · Issue · @davidsgrogan · 💬1 · F2F
- [w3c/aria#2915](https://github.com/w3c/aria/issues/2915) Introduction to AT Driver  
  updated · Issue · @jugglinmike · 💬1 · F2F
- [w3c/aria-practices#3475](https://github.com/w3c/aria-practices/pull/3475) docs(keyboard): correct wording of keyboard support to match working example and code  
  opened · PR · @NickDJM · 💬0
  > The purpose of this PR is to resolve the discrepancy between what the keyboard support _says_ to do vs. what the working example and code actually does in the [Example Disclosure Navigation Menu pattern](https://www.w3.org/WAI/ARIA/apg/patterns/disclosure/examples/disclosure-navigation/). The [Example Disclosure Navigation Menu with Top-Level Links](https://www.w3.org/WAI/ARIA/apg/patterns/disclos…
- [w3c/aria-practices#2991](https://github.com/w3c/aria-practices/pull/2991) Add Practice Page for Supporting Color Contrast Settings  
  updated · PR · @mcking65 · 💬69
- [w3c/aria-practices#1632](https://github.com/w3c/aria-practices/issues/1632) Example Disclosure for Navigation Menus: keyboard support table is inaccurate  
  updated · Issue · @jscholes · 💬4
- [w3c/aria-practices#1390](https://github.com/w3c/aria-practices/issues/1390) Disclosure for Navigation keybindings don't match example functionality  
  updated · Issue · @NickDJM · 💬2
- [w3c/accname#255](https://github.com/w3c/accname/issues/255) Inappropriate example in Text Equivalent Computation 2.1.2  
  updated · Issue · @neet · 💬11 · Agenda
- [w3c/accname#148](https://github.com/w3c/accname/issues/148) Clarification of behavior for "native host language text alternative element" in step 2A  
  updated · Issue · @jaragunde · 💬5
- [w3c/html-aam#370](https://github.com/w3c/html-aam/issues/370) Consider: hidden <label> can still name associated form control  
  closed · Issue · @scottaohara · 💬16 · accName & Desc
- [w3c/html-aria#612](https://github.com/w3c/html-aria/issues/612) Simplify allowances for explicit declaration of implicit role on elements  
  opened · Issue · @scottaohara · 💬2 · Allowed roles, needs changelog entry
  > It is still generally unnecessary for authors to explicitly declare an element's implicit role with ARIA. E.g., `<button role=button>` is redundant and practically useless... but it is also not harmful to accessibility. Rather than declare that is 'not recommended' over and over again, I'm suggesting these redundant statements be removed from the spec. Instead, if it is known that declaring a role…
- [w3c/html-aria#610](https://github.com/w3c/html-aria/issues/610) <figcaption> implicit role  
  opened · Issue · @ZoeBijl · 💬1 · Clarification needed
  > according to the editor’s draft the [figcaption element has no implicit role](https://w3c.github.io/html-aria/#el-figcaption): | element | implicit role | notes | | -------- | ------------ | -----| | figcaption | No corresponding role | Roles: [group](https://w3c.github.io/html-aria/#index-aria-group), [none](https://w3c.github.io/html-aria/#index-aria-none) or [presentation](https://w3c.github.io…
- [w3c/html-aria#615](https://github.com/w3c/html-aria/pull/615) Add allowances for the newly proposed poster element  
  opened · PR · @scottaohara · 💬0 · Allowed roles, Allowed aria-* attributes, New HTML Element, needs changelog entry
  > Matches picture element allowances, as there should be no valid use case for an author to modify this element's role with ARIA, unless they were to be using it incorrectly per its defined use in HTML. Closes #608 Once the feature lands in HTML, inform the following a11y checkers of this update to ARIA in HTML - [ ] [TODO HTML validator](https://github.com/validator/validator/issues/) - [ ] [TODO I…
- [w3c/html-aria#611](https://github.com/w3c/html-aria/pull/611) Update implicit role for figcaption  
  opened · PR · @scottaohara · 💬0
  > closes #610 Editorial: fixes the outdated implicit role info for the `figcaption` element. Normative: indicates that `caption` is an allowed role to specify on the `figcaption` element, but that it is _not recommended_. *** <a href="https://pr-preview.s3.amazonaws.com/w3c/html-aria/pull/611.html" title="Last updated on Oct 23, 2026, 6:52 PM UTC (9f33a2a)">Preview</a> | <a href="https://pr-preview.…
- [w3c/html-aria#614](https://github.com/w3c/html-aria/issues/614) Clarify dd mappings and dt allowed roles  
  opened · Issue · @scottaohara · 💬0 · Allowed roles
  > the `dd` and `dt` allowed roles should match each other additionally, they should have rules similar to the `li` element - where if they are being used within a proper `dl` markup pattern, then no roles should be allowed. And if someone has overwritten the `dl` element's role, then any role should be allowed (that is appropriate in context of their new a11y parent / ancestor relationship) There ar…
- [w3c/html-aria#613](https://github.com/w3c/html-aria/pull/613) Editorial: Update implicit role for mark element  
  opened · PR · @scottaohara · 💬0
  > closes #609 This updates the informative reference for the `mark` element's implicit role. **Note:** I have purposefully not included the typical 'not recommended' wording for redeclaring the element's implicit `mark` role. See https://github.com/w3c/html-aria/issues/612 for why *** <a href="https://pr-preview.s3.amazonaws.com/w3c/html-aria/pull/613.html" title="Last updated on Oct 23, 2026, 6:30 …
- [w3c/html-aria#539](https://github.com/w3c/html-aria/issues/539) Missing roles for dt, dl, dd  
  updated · Issue · @JAWS-test · 💬5
- [w3c/html-aria#600](https://github.com/w3c/html-aria/issues/600) Clarify what "valid figcaption" means for figure  
  updated · Issue · @straker · 💬3
- [w3c/html-aria#608](https://github.com/w3c/html-aria/issues/608) Add Proposed Video Poster Element to the ARIA in HTML Specification  
  updated · Issue · @scottjehl · 💬2 · New HTML Element
- [w3c/aria-at#1421](https://github.com/w3c-cg/aria-at/issues/1421) Design a way to test when automated setup is not possible  
  opened · Issue · @mcking65 · 💬0 · enhancement, tests, test-runner
  > As described in #1415, there are situations where JavaScript cannot complete the setup necessary to create the target test conditions. In this particular case, it is necessary to put the screen reader reading cursor on a disabled element. This can't be done via JavaScript because a disabled element can't be focused. There may be other test conditions where the element being tested can't be made fo…
- [w3c/aria-at#1363](https://github.com/w3c-cg/aria-at/issues/1363) Netlify preview not working for pull requests  
  updated · Issue · @mcking65 · 💬9 · bug
- [w3c/aria-at#1396](https://github.com/w3c-cg/aria-at/issues/1396) Create reusable test modules for APG and HTML-AAM tests  
  updated · Issue · @lolaodelola · 💬4 · Agenda+App Development
- [w3c/aria-at#1402](https://github.com/w3c-cg/aria-at/issues/1402) TPAC Breakout: ARIA-AT Test Writing Workshop  
  updated · Issue · @lolaodelola · 💬3 · Agenda+Test Writing

### APA / 水平レビュー

- [w3c/a11y-request#193](https://github.com/w3c/a11y-request/issues/193) css-color-5 2026-10-20 > 2026-12-20  
  opened · Issue · @svgeesus · 💬0 · LC, REVIEW REQUESTED, pending, s:css-color-5
  > - name of spec to be reviewed: **CSS** Color Module Level 5 - shortname: css-color-5 - URL of spec: https://www.w3.org/TR/2026/WD-css-color-5-20260913/ - What and when is your next expected transition? - To CR Snapshot, Dec 2026 or Jan 2027 - What has changed since any previous review? - [Previous review](https://github.com/w3c/csswg-drafts/issues/7297) was 2022 - [List of changes](https://www.w3.…
- [w3c/a11y-request#188](https://github.com/w3c/a11y-request/issues/188) [ig/security] Security Interest Group Charter  
  closed · Issue · @w3cbot · 💬1 · charter
- [w3c/csswg-drafts#14477](https://github.com/w3c/csswg-drafts/issues/14477) [css-fonts][mediaqueries-5] Add prefers-bold-text user preference media feature  
  updated · Issue · @gregoryd · 💬13 · mediaqueries-5, a11y-tracker, css-fonts-5, Agenda+ TPAC
- [w3c/csswg-drafts#14616](https://github.com/w3c/csswg-drafts/issues/14616) [mediaqueries-5] User preference for limiting HDR brightness (prefers-reduced-peak-brightness / prefers-dynamic-range)  
  updated · Issue · @upadhyayprakash · 💬0 · mediaqueries-5, a11y-tracker, css-color-hdr-1

### WHATWG

- [whatwg/html#13070](https://github.com/whatwg/html/pull/13070) Editorial: fix undefined variable when creating a Document  
  merged · PR · @shannonbooth · 💬0
  > *** <a href="https://whatpr.org/html/13070/document-lifecycle.html" title="Last updated on Oct 13, 2026, 10:02 PM UTC (023efa7)">/document-lifecycle.html</a> ( <a href="https://whatpr.org/html/13070/98753fa...023efa7/document-lifecycle.html" title="Last updated on Oct 13, 2026, 10:02 PM UTC (023efa7)">diff</a> )
- [whatwg/html#13116](https://github.com/whatwg/html/issues/13116) Can a focusable element match `:active` if it has no activation behavior?  
  opened · Issue · @cdoublev · 💬1
  > ### What is the issue with the HTML Standard? The [spec](https://html.spec.whatwg.org/multipage/semantics-other.html#selector-active) requires using this first relevant entry to determine if an element is being activated: > [...] an HTML user agent must use the first relevant entry in the following list > > - **[...]** > - **If the element is focusable** > > The element is being activated if it is…
- [whatwg/html#13138](https://github.com/whatwg/html/pull/13138) Recheck document activity after the dialog beforetoggle event  
  opened · PR · @JinDX · 💬0
  > Recheck that the dialog node document is fully active after firing beforetoggle when showing a modal dialog. A listener can remove a containing iframe. The dialog can remain connected to its own Document even though that Document is no longer fully active. Without this guard, adding open skips the dialog setup steps, and the following close-watcher assertion fails. Suggested regression coverage: r…
- [whatwg/html#13133](https://github.com/whatwg/html/pull/13133) Fix the event variable in the navigation interception example  
  opened · PR · @JinDX · 💬0
  > Use e.destination.url in the navigation interception example. The listener parameter and all other event accesses in that example use e. This avoids relying on the legacy global event property. Spec: https://html.spec.whatwg.org/multipage/nav-history-apis.html#navigation-api-intro - [ ] At least two implementers are interested (and none opposed): * … * … - [ ] [Tests](https://github.com/web-platfo…
- [whatwg/html#13127](https://github.com/whatwg/html/pull/13127) Compare popover attribute states consistently  
  opened · PR · @JinDX · 💬0
  > Compare originalType with the current state of the popover attribute. originalType is initialized from the attribute state, but the later guard currently compares it with the attribute value. This keeps the guard meaningful for values such as the empty string that map to the Auto state. Suggested regression coverage: equivalent attribute spellings and state changes caused by beforetoggle handlers …
- [whatwg/html#13126](https://github.com/whatwg/html/pull/13126) Guard a null ancestor when showing a hint popover  
  opened · PR · @JinDX · 💬0
  > Check that ancestor is not null before reading its opened in popover mode when assigning the hint stack parent. The topmost popover ancestor algorithm can return null, including for a standalone hint popover. Suggested regression coverage: showing a hint popover without an open popover ancestor, and showing one under an auto popover. Spec: https://html.spec.whatwg.org/multipage/popover.html#show-p…
- [whatwg/html#13119](https://github.com/whatwg/html/pull/13119) Focus the viewport when closing a dialog without previous focus  
  opened · PR · @hjanuschka · 💬0
  > When a dialog closes without a previously focused element, its current focus can remain inside the closed dialog until the asynchronous focus fixup runs. Focus the document's viewport synchronously if focus is still inside the dialog; leave focus elsewhere alone. Fixes #13118. - [ ] At least two implementers are interested (and none opposed). - [ ] [Tests](https://github.com/web-platform-tests/wpt…
- [whatwg/html#13118](https://github.com/whatwg/html/issues/13118) Reset focus when closing a dialog with no previously focused element  
  opened · Issue · @hjanuschka · 💬0
  > The [close-the-dialog algorithm](https://html.spec.whatwg.org/multipage/interactive-elements.html#close-the-dialog) restores `previously focused element` if non-null, but does nothing with focus when it is null. If focus is inside the dialog when it closes, this leaves the focused area inside a closed dialog until the [asynchronous focus fixup rule](https://html.spec.whatwg.org/multipage/webappapi…
- [whatwg/html#13105](https://github.com/whatwg/html/issues/13105) Should `focus-without-user-activation` be able to allow cross-origin autofocus?  
  opened · Issue · @ffiori · 💬0
  > ### What is the issue with the HTML Standard? ## Summary Should an allowed `focus-without-user-activation` policy lift the cross-origin restriction on declarative `autofocus`, or should that restriction remain independent of the policy? ## Current specification and test The [autofocus insertion algorithm][autofocus] invokes the **allow focus steps**. In [#11277][spec-pr], I removed the additional …
- [whatwg/html#13104](https://github.com/whatwg/html/issues/13104) HTML integration for document.advanceFocus() and beforefocus  
  opened · Issue · @mshoho · 💬0 · addition/proposal, needs implementer interest
  > ### What problem are you trying to solve? Keyboard users need predictable navigation through composite controls, including controls containing third-party web components or embedded documents. Applications sometimes need to choose an entry point or move to the next control using the browser's existing sequential focus order, without reconstructing that order in JavaScript or changing the DOM to in…
- [whatwg/html#13050](https://github.com/whatwg/html/pull/13050) Add the focusreset event  
  updated · PR · @noamr · 💬7
- [whatwg/html#13045](https://github.com/whatwg/html/pull/13045) Don't hide popovers that moved document while hiding a popover stack  
  updated · PR · @jakearchibald · 💬6 · needs tests

### ブラウザ / AT

- [web-platform-tests/interop-accessibility#256](https://github.com/web-platform-tests/interop-accessibility/issues/256) Should we store Gen AI skills/tools related to accessibility WPT efforts?  
  opened · Issue · @cookiecrook · 💬0
  > I noticed there were a bunch of accessibility-related tests in WPT that didn't have the accessibility labels, so they weren't showing up in searches like this one: https://wpt.fyi/results/?label=master&label=experimental&aligned&q=label%3Aaccessibility So I used Claude to find and add them in this now-merged PR. https://github.com/web-platform-tests/wpt-metadata/pull/9537 As part of that effort, I…
- [web-platform-tests/interop-accessibility#246](https://github.com/web-platform-tests/interop-accessibility/issues/246) Meeting: October 7, 2026, @ 9 AM PST  
  closed · Issue · @zcorpan · 💬5
- [web-platform-tests/interop-accessibility#202](https://github.com/web-platform-tests/interop-accessibility/issues/202) Interop 2026 Accessibility Investigation  
  updated · Issue · @zcorpan · 💬13 · Agenda+, 2026-investigation-candidate
- [web-platform-tests/interop-accessibility#214](https://github.com/web-platform-tests/interop-accessibility/issues/214) svg-mouse-listener crashtest file is outside the crashtests directory  
  updated · Issue · @cookiecrook · 💬1 · good first issue
- [web-platform-tests/interop-accessibility#250](https://github.com/web-platform-tests/interop-accessibility/issues/250) Write tests for CSS generated content with alt text (::before/::after and ::marker)  
  updated · Issue · @zcorpan · 💬1 · Agenda+
- [web-platform-tests/interop#1333](https://github.com/web-platform-tests/interop/issues/1333) Reference Target for Cross-Root ARIA  
  updated · Issue · @davatron5000 · 💬2 · focus-area-proposal

## 2. 議事録

- 2026-10-19 COGA TF: https://www.w3.org/2026/10/19-coga-minutes.html
- 2026-10-20 AGWG: https://www.w3.org/2026/10/20-ag-minutes.html
- 2026-10-21 APA WG: https://www.w3.org/2026/10/21-apa-minutes.html
- 2026-10-21 ARIA-AT CG: https://www.w3.org/2026/10/21-aria-at-minutes.html

## 3. フィード

(なし)

## 4. リリース

- [nvaccess/nvda release-2026.3rc1](https://github.com/nvaccess/nvda/releases/tag/release-2026.3rc1) (pre) (2026-10-21)  
  * Highlights can be found in the [release blog post](https://www.nvaccess.org/post/nvda-2026-3rc1/). * [VirusTotal scan results](https://www.virustotal.com/gui/file-analysis/MDM1NWZmNDA4ZmZlZjdkNTYwNGMxMTk5NDBkNzI5YjA6MTc5MjU0MTMzOA==/detection) * SHA256 sum: `f233fe4c2134560c3b945e94ce4c1835a62c511
- [nvaccess/nvda release-2026.3beta6](https://github.com/nvaccess/nvda/releases/tag/release-2026.3beta6) (pre) (2026-10-19)  
  * Highlights can be found in the [release blog post](https://www.nvaccess.org/post/nvda-2026-3beta6/). * [VirusTotal scan results](https://www.virustotal.com/gui/file-analysis/NzdmZmJjMWE4NGE2MzY1MDA0ZjBjYWE4NmU5ZWIwNTk6MTc5MjM4MjA4NA==/detection) * SHA256 sum: `407cd4afb19d72b533c7a88a7eda86fb38d8a
- [oxc-project/oxc oxlint_v1.89.0](https://github.com/oxc-project/oxc/releases/tag/oxlint_v1.89.0) (2026-10-19)  
  - d7c6b26 linter: Mark jsx-a11y rules as recommended (#27690) (Cam McHenry)
- [GoogleChrome/modern-web-guidance v0.0.195](https://github.com/GoogleChrome/modern-web-guidance/releases/tag/v0.0.195) (2026-10-19)  
  * Introduced a new guide for **[icons](https://github.com/GoogleChrome/modern-web-guidance/blob/v0.0.195/skills/modern-web-guidance/guides/ui-atoms/icons.md)** outlining performant, scalable, and accessible best practices for embedding and rendering SVG icons across modern web interfaces. * Added a 

## 5. 新規リポジトリ

- [littlebordercollie/mcd-together-order](https://github.com/littlebordercollie/mcd-together-order) ★100 JavaScript — 麦麦一起点：培智学生用图片表达选择，家长接手核对。麦当劳 MCP 点餐沟通原型。  
  topics: accessibility, mcp, special-education
- [aidenleads/css-animation-snippets](https://github.com/aidenleads/css-animation-snippets) ★62 CSS — Free copy-paste CSS animations for business websites. No frameworks, no build step, accessible by default. Love Yall ❤️  
  topics: css, css-animations, free-resources, frontend, small-business, ui, web-design
- [UltimateBursar24/alt-text](https://github.com/UltimateBursar24/alt-text) ★24 C# — Published: 2026-10-18  
  topics: accessibility, ai-tools, alt-text, batch-processing, csharp, csv-export, dotnet, image-captioning
- [we1jia/AgentDock](https://github.com/we1jia/AgentDock) ★19 Rust — A Liquid Glass voice speed-dial for your AI agents — call, mute, hang up and switch between ChatGPT dot, Grok Bot, Copilot, Devin and more. macOS, Tauri 2 + Rust.  
  topics: accessibility, ai-agents, chatgpt, desktop-app, grok, liquid-glass, macos, rust
- [StylistPucker/read-aloud](https://github.com/StylistPucker/read-aloud) ★18  — Published: 2026-10-18  
  topics: accessibility, audiobook-export, balabolka-alternative, clipboard-reader, csharp, dotnet, epub, mit-license
- [TurnOver-For-Mac/turnover](https://github.com/TurnOver-For-Mac/turnover) ★13 Swift — A screen reader for the Mac that works alongside VoiceOver. Free and open source.  
  topics: accessibility, macos, screen-reader, swift, voiceover
- [maddhruv/pristine](https://github.com/maddhruv/pristine) ★13 Astro — Agent skill that critiques, designs and polishes web UI to 10/10, judged through your users' eyes.  
  topics: accessibility, agent-skills, claude-code, design, frontend, ui, ux
- [Barabosik/one-shot-site](https://github.com/Barabosik/one-shot-site) ★11 JavaScript — Answer a few multiple-choice questions. Your agent builds a finished website, checks it in a real browser at phone and desktop size, and puts it online. A free agent skill, MIT.  
  topics: accessibility, agent-skills, ai-agents, claude-code, claude-code-plugin, claude-skills, codex, github-pages
- [my12yyds/modfx-accessibility](https://github.com/my12yyds/modfx-accessibility) ★10 Python — A draft manifest and dependency-free validator for visual-effect accessibility controls in Minecraft mods.  
  topics: accessibility, cli, json-schema, minecraft, modding, python
- [kayson-39/YishengTranslator-White](https://github.com/kayson-39/YishengTranslator-White) ★9 Python — 译声实时翻译（白色新版）— 免费的 Windows 实时日语字幕与翻译工具，支持系统声音、本地 GGUF / Ollama / OpenAI 兼容 API 翻译。  
  topics: accessibility, desktop-app, gguf, japanese, llama-cpp, pyside6, real-time, speech-recognition
- [codewithasnari/nongeneric](https://github.com/codewithasnari/nongeneric) ★9 JavaScript — Anti-slop design + GSAP motion skill pack for AI coding agents, with an 82-rule UI detector.  
  topics: accessibility, agent-skills, ai-agents, claude-code, cli, codex, cursor, design-system
- [spcaeo/toadstone](https://github.com/spcaeo/toadstone) ★7 Python — A self-hosted alternative to Screaming Frog: your crawl, your machine, no per-URL pricing and no seats. 222 SEO checks — 180 of them proven to fire against a site built to be wrong. JS rendering, craw…  
  topics: accessibility, axe-core, core-web-vitals, crawler, docker, flask, log-file-analysis, mcp
- [bytebeast/kissaten.nvim](https://github.com/bytebeast/kissaten.nvim) ★7 Lua — Coffee-house Neovim colorscheme. WCAG-checked, LazyVim-ready, 5 styles. Code theme with Treesitter, LSP semantic tokens, 46+ plugin integrations, lualine and terminal themes.  
  topics: accessibility, catppuccin, color-scheme, colorblind, colorscheme, dark-theme, ghostty, lazyvim
- [tomatoparkdao/registered-architect](https://github.com/tomatoparkdao/registered-architect) ★7 Python — OmniAiLab Registered Architect｜全球注册建筑师专业 Skill，也是会引导你做判断的规范决策系统：先定项目所在地与适用法规（中/美/英/德/日/新/澳/印/阿联酋/沙特），再走方案、技术设计、消防、无障碍、节能与施工图，输出可追溯的设计判断与条文核验清单。A code-driven architecture Skill for licensed architects …  
  topics: accessibility, ada, aec, architecture, bim, building-codes, building-design, code-compliance
- [alphaparkinc/genpark-multimodal-palette-color-blindness-simulator-skill](https://github.com/alphaparkinc/genpark-multimodal-palette-color-blindness-simulator-skill) ★7 Python — Multimodal accessibility engine simulating Protanopia, Deuteranopia, and Tritanopia color vision deficiencies  
  topics: agent-skills, ai-agent, anomaly-detector, color-blindness, jitter-buffer, mcp, mcp-server, model-context-protocol
- [Alpha-Park/genpark-multimodal-palette-color-blindness-simulator-skill](https://github.com/Alpha-Park/genpark-multimodal-palette-color-blindness-simulator-skill) ★7 Python — Multimodal accessibility engine simulating Protanopia, Deuteranopia, and Tritanopia color vision deficiencies  
  topics: agent-skills, ai-agent, anomaly-detector, color-blindness, jitter-buffer, mcp, mcp-server, model-context-protocol
- [Alpha-Park/genpark-multimodal-hsv-color-palette-extractor-skill](https://github.com/Alpha-Park/genpark-multimodal-hsv-color-palette-extractor-skill) ★7 Python — Multimodal design palette extractor analyzing RGB-to-HSV histograms and WCAG 2.1 contrast ratios  
  topics: agent-skills, ai-agent, chargeback-defense, hsv-palette, mcp, mcp-server, model-context-protocol, payload-fuzzing
- [alphaparkinc/genpark-multimodal-hsv-color-palette-extractor-skill](https://github.com/alphaparkinc/genpark-multimodal-hsv-color-palette-extractor-skill) ★7 Python — Multimodal design palette extractor analyzing RGB-to-HSV histograms and WCAG 2.1 contrast ratios  
  topics: agent-skills, ai-agent, chargeback-defense, hsv-palette, mcp, mcp-server, model-context-protocol, payload-fuzzing
- [abhayymishraa/sightline](https://github.com/abhayymishraa/sightline) ★6 Swift — Type where you look. Your webcam moves keyboard focus to the screen, window or pane you face. macOS and Windows.  
  topics: accessibility, eye-tracking, focus, head-tracking, macos, multi-monitor, open-source, productivity
- [luckeyfaraday/phone-use](https://github.com/luckeyfaraday/phone-use) ★6 JavaScript — Let AI agents use an Android phone or iPhone: read the screen, tap, type, scroll and take screenshots. MCP server + CLI, with consent on the phone.  
  topics: accessibility, adb, ai-agents, android, android-automation, claude, codex, ios
- [Synapsr/Parler](https://github.com/Synapsr/Parler) ★6 TypeScript — Open-source voice dictation app for macOS, Windows and Linux. Hold a shortcut, speak, and your words are typed in any app. Cloud speech-to-text with Groq, OpenAI, Fireworks or any Whisper-compatible s…  
  topics: accessibility, dictation, groq, linux, macos, open-source, openai, productivity
- [ShouldBeQuincy/LectureFlow](https://github.com/ShouldBeQuincy/LectureFlow) ★6 Go — A simple-looking, not-so-simple lecture transcription and translation tool. Maybe more. ｜ 一个简约但不太简单的讲座听写与翻译工具，或许还有更多。  
  topics: accessibility, apple-silicon, assistive-technology, bilingual-subtitles, desktop-app, education, electron, faster-whisper
- [youssef4laa/artistic-color-palettes](https://github.com/youssef4laa/artistic-color-palettes) ★6 Python — Real artistic colour palettes (Wada plates, Heian kasane, public-domain paintings) turned into OKLCH ramps, design tokens, measured contrast and a composed dark mode. Agent Skill + Claude Code plugin.  
  topics: agent-skills, apca, claude-code, claude-skills, color-palette, dark-mode, design-tokens, oklch
- [tripolskiydigital/onepluscontrolcenter](https://github.com/tripolskiydigital/onepluscontrolcenter) ★6 Kotlin — OxygenOS 16 notification shade and control center rebuilt for Google Pixel, no root (Jetpack Compose, accessibility overlay, optional Shizuku)  
  topics: 
- [izynu/ochrelle](https://github.com/izynu/ochrelle) ★6 TypeScript — Give AI a design sense. 28 open-source Agent Skills for interface art direction: 1 master skill that picks the right visual style, 27 specialists that execute it with production-quality guidance and W…  
  topics: agent-skills, ai, design, design-system, design-systems, design-tool, design-tools, front-end
- [priyanshusta/ZEHEN](https://github.com/priyanshusta/ZEHEN) ★5 Python — Free, open source hand-gesture and voice control for Windows. Webcam gestures move the cursor; say Zehen and an AI assistant opens apps, clicks, types and answers out loud. Offline wake word, no extra…  
  topics: accessibility, ai-assistant, computer-vision, gesture-control, hand-tracking, hands-free, handwriting-recognition, hci
- [mvcompany8500-web/sasarisa](https://github.com/mvcompany8500-web/sasarisa) ★5 Swift — The AI assistant you just talk to (사사리사) — free, open-source voice assistant for macOS. Name it, say it: chores done on your Mac, coding handed to the AI you use (Claude Code, Codex, Aside, API or loc…  
  topics: accessibility, ai-assistant, claude-code, korean, macos, macos-app, sasarisa, speech-recognition
- [Mir-Zairan/shoga-speaks](https://github.com/Mir-Zairan/shoga-speaks) ★5 JavaScript — 🦜 Claude Code plugin that explains everything in your language, script and role: Roman-Urdu, Urdu, Hinglish, Hindi, Dutch. Plain-language approvals, failure explanations, quality checks.  
  topics: accessibility, ai-coding-assistant, anthropic, claude, claude-code, claude-code-plugin, code-review, developer-experience
- [fdeox/deonyx](https://github.com/fdeox/deonyx) ★4 Rust — Dark mode for any Windows app. Free, flicker-free, and your 3D views keep their real colors.  
  topics: accessibility, dark-mode, darkmode, night-mode, rust, sketchup, tauri, windows
- [ConquerorX/arcodownloader](https://github.com/ConquerorX/arcodownloader) ★4 JavaScript — 🎵 ARCOD Grab — player.arcod.xyz için sayfa içi FLAC/MP3 indirme paneli (MV3 tarayıcı eklentisi)  
  topics: accessibility, browser-extension, chrome-extension, downloader, flac, hi-res-audio, javascript, manifest-v3
- [MHusted01/shortcutlens](https://github.com/MHusted01/shortcutlens) ★4 Swift — Hold Command to see the keyboard shortcuts of the frontmost macOS app. No telemetry.  
  topics: accessibility, appkit, cheatsheet, keyboard-shortcuts, macos, macos-app, menu-bar-app, menubar
- [DEVAL-020/depth-ui](https://github.com/DEVAL-020/depth-ui) ★4 TypeScript — A modern, accessible React & Tailwind CSS component library with 100+ interactive primitives, 3D spatial cards, and smooth micro-animations.  
  topics: components, design-system, framer-motion, react, tailwind, typescript, ui-components, ui-library
- [sti7an/awesome-ui-ux](https://github.com/sti7an/awesome-ui-ux) ★3  — Whether you're a designer, developer, product manager, or simply a curious mind — this list is your one-stop home for everything UI & UX.  
  topics: a11y, accessibility, awesome, awesome-list, awesome-lists, awesome-readme, design-system, design-tools
- [anon5376/fine-design](https://github.com/anon5376/fine-design) ★3 TypeScript — React design system on Base UI, Tailwind v4 and Motion, shipped as a shadcn registry: 42 components, 7 blocks, three themes, and a Claude Code plugin. MIT.  
  topics: accessibility, agent-skills, base-ui, claude-code-plugin, design-system, mcp, motion, nextjs
- [sarmadiq9090-coder/Remember-Me](https://github.com/sarmadiq9090-coder/Remember-Me) ★3 JavaScript — Free, open-source task, note and reminder app for Windows: sticky reminders, flexible repeats, 12 languages, themes and offline-first storage.  
  topics: accessibility, desktop-app, electron, electron-app, english, i18n, multilingual, notes
- [CeyhunOzcorapsiz/the-booth](https://github.com/CeyhunOzcorapsiz/the-booth) ★3 Python — An AI broadcast crew that gives every fan their own fact-checked live football broadcast. Microsoft x Premier League Inside the Game hackathon.  
  topics: accessibility, azure, fastapi, football, hackathon, microsoft-agent-framework, microsoft-foundry, multi-agent
- [jacobjmarks/speak](https://github.com/jacobjmarks/speak) ★3 Python — Private, offline voice dictation for any app. Hold a key, speak, and tidy text is typed for you. Free and open source.  
  topics: accessibility, asr, desktop-app, dictation, llama-cpp, local-first, local-llm, nemotron
- [OrchestraTech/BeethovenInterface](https://github.com/OrchestraTech/BeethovenInterface) ★3 Python — Mediapipe Based Eye To Mouse Interface  
  topics: accessibility, computer-vision, computer-vision-opencv, eye-tracking, eye-tracking-mouse, mediapipe, mediapipe-facemesh, opencv
- [sanjayadanushka712/Dracula-Deep](https://github.com/sanjayadanushka712/Dracula-Deep) ★3 Python — A low-glare Dracula-inspired VS Code theme with measured WCAG AA contrast, muted UI accents, and six-step bracket-depth highlighting.  
  topics: accessibility, color-theme, dark-theme, dracula, low-contrast, theme, vscode, vscode-extension
- [sylhetyhackvenger/RootEye](https://github.com/sylhetyhackvenger/RootEye) ★3 Shell — RootEye — View Element eXtractor by SYLHETYHACKVENGER (THE-ERROR808): A root-powered, terminal-only Android recon tool for Termux. Live foreground app tracking, UI element extraction, notifications, c…  
  topics: deep-research, developer-mode, element-reader, element-ui, eye-tracking, forensic-analysis, forensics-tools, gray-hat-hacking-tools
- [benhuang3/accessibility-anywhere](https://github.com/benhuang3/accessibility-anywhere) ★3 Python —   
  topics: 
- [AyberkA0/oz-wm-macos](https://github.com/AyberkA0/oz-wm-macos) ★3 Swift — Better workspaces for macOS. Vertically scrolling tiling, as an app on top of the Accessibility API.  
  topics: 
- [joaquimftt-web/terra-motion-skills](https://github.com/joaquimftt-web/terra-motion-skills) ★3 TypeScript — Reusable React motion components, design tokens, and AI agent skills for accessible interface interactions.  
  topics: acessibility, agent-skills, animations, motion, motion-design, react, typescript, ui-components
- [izynu/Weftline](https://github.com/izynu/Weftline) ★3 TypeScript — A research-backed five-pass workflow and installable Agent Skill for thoughtful, accessible frontend work.  
  topics: accessibility, agent-skills, ai-agents, developer-tools, frontend, nextjs, typescript, web-development

### 活発な既存リポジトリ (stars≥200, 期間内に push)

- [chakra-ui/chakra-ui](https://github.com/chakra-ui/chakra-ui) ★40708 — Chakra UI is a component system for building SaaS products with speed ⚡️
- [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) ★30002 — PDF Parser for AI-ready data. Automate PDF accessibility. Open-source.
- [markmead/hyperui](https://github.com/markmead/hyperui) ★12269 — Free Tailwind CSS v4 components for your next project, designed to enhance your web development with the latest features and styles 🚀
- [webstudio-is/webstudio](https://github.com/webstudio-is/webstudio) ★9109 — Open source website builder and Webflow alternative. Webstudio is an advanced visual builder that connects to any headless CMS, supports all CSS properties, and can be hosted anywhere, including with …
- [ariakit/ariakit](https://github.com/ariakit/ariakit) ★8630 — Toolkit with accessible components, styles, and examples for your next web app
- [grommet/grommet](https://github.com/grommet/grommet) ★8352 — a react-based framework that provides accessibility, modularity, responsiveness, and theming in a tidy package
- [dequelabs/axe-core](https://github.com/dequelabs/axe-core) ★7705 — Accessibility engine for automated Web UI testing
- [miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop) ★7169 — Rules for an AI coding agent to filter out generic AI-generated UI designs, text, and code.
- [skeletonlabs/skeleton](https://github.com/skeletonlabs/skeleton) ★6083 — Skeleton is an adaptive design system powered by Tailwind CSS.
- [chakra-ui/zag](https://github.com/chakra-ui/zag) ★5239 — Build your design system in React, Solid, Vue, Svelte or Vanilla. Powered by finite state machines
- [nvaccess/nvda](https://github.com/nvaccess/nvda) ★2668 — NVDA, the free and open source Screen Reader for Microsoft Windows
- [KittyGiraudel/a11y-dialog](https://github.com/KittyGiraudel/a11y-dialog) ★2490 — A very lightweight and flexible accessible modal dialog script.
- [Fate-Grand-Automata/FGA](https://github.com/Fate-Grand-Automata/FGA) ★2410 — Auto-battle app for F/GO Android
- [lahfir/agent-desktop](https://github.com/lahfir/agent-desktop) ★1821 — Agent Desktop gives any agent reliable computer use on the desktop. Built with Rust, it sees any app's real UI structure through OS accessibility trees and operates it — refs stay stable and actions s…
- [ken107/read-aloud](https://github.com/ken107/read-aloud) ★1783 — An awesome browser extension that reads aloud webpage content with one click
- [ankit/stylebot](https://github.com/ankit/stylebot) ★1701 — Restyle any website
- [yamada-ui/yamada-ui](https://github.com/yamada-ui/yamada-ui) ★1034 — React UI components of the Yamada, by the Yamada, for the Yamada built with React and Emotion.
- [vue-final/vue-final-modal](https://github.com/vue-final/vue-final-modal) ★1013 — 🍕Vue Final Modal is a tiny, renderless, mobile-friendly, feature-rich modal component for Vue.js.
- [VocaHQ/vocalinux](https://github.com/VocaHQ/vocalinux) ★965 — Free, open-source, 100% offline voice dictation for Linux. Speak and type anywhere via whisper.cpp, Whisper & VOSK engines, GPU-accelerated, works on X11 + Wayland!
- [lukasbach/headless-tree](https://github.com/lukasbach/headless-tree) ★909 — The definitive tree component for the Web
- [y3owk1n/neru](https://github.com/y3owk1n/neru) ★865 — Hints, grids and vim keys for your whole desktop. Built for macOS, linux and windows, natively.
- [lxsmnsyc/terracotta](https://github.com/lxsmnsyc/terracotta) ★706 — Headless UI for SolidJS
- [AgentiLoop/Agent](https://github.com/AgentiLoop/Agent) ★649 — Agent! now supports macOS 14.6 or later, Apple Silicon and Intel, latest release. The Best AI agent for Mac: drives any app via Accessibility, codes/builds in Xcode, automates AppleScript, JXA, Swift …
- [focus-trap/tabbable](https://github.com/focus-trap/tabbable) ★625 — Find descendants of a DOM node that are in the tab order
- [guidepup/guidepup](https://github.com/guidepup/guidepup) ★585 — Screen reader automation library for testing.
- [vmware-clarity/ng-clarity](https://github.com/vmware-clarity/ng-clarity) ★433 — Clarity Angular is a scalable, accessible, customizable, open-source design system built for Angular.
- [toyota-connected/ivi-homescreen](https://github.com/toyota-connected/ivi-homescreen) ★401 — Flutter Linux C++ embedder for desktop and embedded/automotive displays — Wayland, DRM/KMS, EGL, Vulkan (incl. zero-copy dma-buf), and software backends
- [cvs-health/ios-swiftui-accessibility-techniques](https://github.com/cvs-health/ios-swiftui-accessibility-techniques) ★387 — Demonstrates iOS SwiftUI Accessibility programming techniques using live good and bad examples that can be tested with VoiceOver and other AT. Includes documentation for developers explaining how to c…
- [CMSgov/design-system](https://github.com/CMSgov/design-system) ★371 — Open source design and front-end development resources for creating Section 508 compliant, responsive, and consistent websites.
- [niki914/zafiro](https://github.com/niki914/zafiro) ★299 — Open-source BYOK AI agent for Android. Full phone control, native Shell & Python 3, with Skills and MCP support. Built with Material 3 Expressive. Works via Shizuku (root optional). Bring any provider…
- [squirrelscan/squirrelscan](https://github.com/squirrelscan/squirrelscan) ★296 — The website QA tool for your coding agent. 300+ audit rules across SEO, performance, security, accessibility and agent experience.
- [public-ui/kolibri](https://github.com/public-ui/kolibri) ★288 — The accessible HTML-Standard
- [nuxt/a11y](https://github.com/nuxt/a11y) ★233 — Nuxt module to provide accessibility hinting and utilities.
- [Samyssmile/notectl](https://github.com/Samyssmile/notectl) ★208 — Modern Accessible WYSIWYG rich text editor built as a framework-agnostic Web Component that works everywhere.
- [vuelessjs/vueless](https://github.com/vuelessjs/vueless) ★207 — A UI Library with Open Architecture for Vue & Nuxt — powered by Storybook and Tailwind CSS 💚
- [saurabhav88/EnviousWispr](https://github.com/saurabhav88/EnviousWispr) ★200 — Free, sub-second on-device AI dictation for macOS. Dual engines (Whisper + Parakeet) on Apple Silicon. Optional AI polish on your Mac with EG-1 or S1-mini by Superwhisper, Apple Intelligence (macOS 26…

## 6. Awesome 系リストへの追加

(なし)

## 取得失敗

(なし)
