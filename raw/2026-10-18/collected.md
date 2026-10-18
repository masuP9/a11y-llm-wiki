# Collected: 2026-10-11 〜 2026-10-18

> scripts/collect.py の自動出力。/weekly コマンドの入力。

## 1. 標準リポジトリの動き

### AGWG / WCAG

- [w3c/wcag#5409](https://github.com/w3c/wcag/issues/5409) In Understanding, replace heading “Key Terms” with “Relevant Glossary Entries” or similar  
  opened · Issue · @yatil · 💬6
  > The Understanding pages have a section called “Key Terms” which are the glossary items that are referenced in the discussed success criterion. These are normative phrases. However the collapsed section and the use of “Key Terms” makes them look as additional and optional. I think it is great to have these definitions on the Understanding pages, but we should make it more clear that these ar (norma…
- [w3c/wcag#5407](https://github.com/w3c/wcag/pull/5407) Change "correct" to "appropriate" in 4.1.2 "in brief"  
  opened · PR · @patrickhlauke · 💬4 · Understanding, 4.1.2 Name Role Value
  > throughout the body of the document, we talk about "appropriate" ... but the "in brief" mentions "correct", which is contentious. it implies that there is always a "correct" name/role/property/state, which is not necessarily the case. a late follow-up to https://github.com/w3c/wcag/pull/2207 (where we put "appropriate" everywhere but missed this one out) diff: https://services.w3.org/htmldiff?doc1…
- [w3c/wcag#5404](https://github.com/w3c/wcag/pull/5404) Make the example for the `role` definition feel more current/relevant  
  opened · PR · @patrickhlauke · 💬1 · ErratumRaised, Normative
  > Closes https://github.com/w3c/wcag/issues/1476
- [w3c/wcag#5403](https://github.com/w3c/wcag/pull/5403) Tweak "programmatically determined" definition example  
  opened · PR · @patrickhlauke · 💬1 · ErratumRaised, Normative
  > Mention "accessibility API" for the first example of markup languages, so it doesn't look like direct access/parsing is the only way in which AT can determine something programmatically (in fact, nowadays I guess no AT does this anymore?) Closes https://github.com/w3c/wcag/issues/3001
- [w3c/wcag#5411](https://github.com/w3c/wcag/pull/5411) non-text-contrast: add clarification on button indication, fix typo  
  opened · PR · @fstrr · 💬1 · 1.4.11 Non-text contrast
  > Closes #865 1. fixes typo 2. adds a paragraph about boundaries 3. edits description for figure 30 [Preview](https://deploy-preview-5411--wcag2.netlify.app/understanding/non-text-contrast) [Diff](https://services.w3.org/htmldiff?doc1=https%3A%2F%2Fwww.w3.org%2FWAI%2FWCAG22%2FUnderstanding%2Fnon-text-contrast.html&doc2=https%3A%2F%2Fdeploy-preview-5411--wcag2.netlify.app%2Funderstanding%2Fnon-text-c…
- [w3c/wcag#5402](https://github.com/w3c/wcag/pull/5402) Note for 2.5.8 Target Size (Minimum) and how 24x24 was chosen  
  opened · PR · @patrickhlauke · 💬1 · Understanding, 2.5.8 Target Size (Minimum)
  > Closes #4178 Preview: https://deploy-preview-5402--wcag2.netlify.app/understanding/target-size-minimum#brief Diff: https://services.w3.org/htmldiff?doc1=https%3A%2F%2Fwww.w3.org%2FWAI%2FWCAG22%2FUnderstanding%2Ftarget-size-minimum.html&doc2=https%3A%2F%2Fdeploy-preview-5402--wcag2.netlify.app%2Funderstanding%2Ftarget-size-minimum
- [w3c/wcag#5408](https://github.com/w3c/wcag/pull/5408) Tweak two of the examples in 3.3.2 Labels or Instructions  
  opened · PR · @patrickhlauke · 💬1 · Understanding, 3.3.2 Labels or instructions
  > * simplifies the example about strict username rules - there's really no reason why it talks about TWO websites? * modify the US phone number example - mention the overarching label earlier, make it clear that we think the punctuation acts as a label. don't mention use of `title`, but `aria-label` instead. and cross-reference 4.1.2 because that aspect of giving an accessible name is NOT the concer…
- [w3c/wcag#882](https://github.com/w3c/wcag/issues/882) Understanding 2.5.3 - actually rendered examples but no markup examples?  
  closed · Issue · @patrickhlauke · 💬4 · WCAG 2.1, Understanding, Needs assigning
- [w3c/wcag#5405](https://github.com/w3c/wcag/issues/5405) [spam]  
  closed · Issue · @tuhinbond9-svg · 💬1
- [w3c/wcag#5318](https://github.com/w3c/wcag/issues/5318) 1.4.5 Move the note embedded in a paragraph to the standard styling  
  closed · Issue · @ljkoakley · 💬1
- [w3c/wcag#5412](https://github.com/w3c/wcag/issues/5412) [spam]  
  closed · Issue · @suuzuali022-gif · 💬0
- [w3c/wcag#5410](https://github.com/w3c/wcag/issues/5410) [spam]  
  closed · Issue · @vovanhieu925-star · 💬0
- [w3c/wcag#5406](https://github.com/w3c/wcag/issues/5406) [spam]  
  closed · Issue · @lardinroselia932-lab · 💬0
- [w3c/wcag#5400](https://github.com/w3c/wcag/issues/5400) [spam]  
  closed · Issue · @umahr086-dot · 💬0
- [w3c/wcag#5373](https://github.com/w3c/wcag/issues/5373) Conforming Alternate Version (CAV) and the mechanism to reach/achieve it  
  updated · Issue · @patrickhlauke · 💬20 · 3.3.2 Labels or instructions, Conformance WCAG 2.x, 2.4.6 Headings and Labels, Response-Only
- [w3c/wcag#855](https://github.com/w3c/wcag/issues/855) Applicability of 2.5.3 Label in Name when no label is present (or just placeholder)  
  updated · Issue · @detlevhfischer · 💬14 · Discussion, WCAG 2.1, 2.5.3 Label in Name
- [w3c/wcag#1476](https://github.com/w3c/wcag/issues/1476) Definition and example for 'role' are confusing  
  updated · Issue · @36degrees · 💬11 · WCAG 2.1, ErratumRaised, WCAG 2.0
- [w3c/wcag#4178](https://github.com/w3c/wcag/issues/4178) 2.5.8 Understanding origin of minimum "24"  
  updated · Issue · @jamieherrera · 💬9 · 2.5.8 Target Size (Minimum)
- [w3c/wcag#5395](https://github.com/w3c/wcag/issues/5395) Reiterate that 4.1.2 is scoped to states/properties *that can be set by the user*  
  updated · Issue · @patrickhlauke · 💬8 · Understanding, 4.1.2 Name Role Value, Substantive
- [w3c/wcag#5119](https://github.com/w3c/wcag/pull/5119) Change 'serialize' to 'linearize' in Note 2 of Consistent Help  
  updated · PR · @bruce-usab · 💬7 · ErratumRaised, 3.2.6 Consistent Help
- [w3c/wcag#5287](https://github.com/w3c/wcag/pull/5287) Update Statement of Partial Conformance  
  updated · PR · @bruce-usab · 💬4 · ErratumRaised, Conformance WCAG 2.x
- [w3c/wcag#4995](https://github.com/w3c/wcag/pull/4995) Clarifications to labels or instructions SC  
  updated · PR · @scottaohara · 💬4 · Understanding, 3.3.2 Labels or instructions, Substantive, Non-Normative
- [w3c/wcag#865](https://github.com/w3c/wcag/issues/865) Clarification on button distinguishing indicator for 1.4.11 Non-text Contrast  
  updated · Issue · @LaurenceRLewis · 💬4 · WCAG 2.1, Understanding, Needs assigning
- [w3c/wcag#5369](https://github.com/w3c/wcag/issues/5369) "Are programming languages human languages?" and repercussions for text contrast requirements  
  updated · Issue · @patrickhlauke · 💬4 · 1.4.3 Contrast (Minimum), 1.4.6 Contrast (Enhanced)
- [w3c/wcag#4906](https://github.com/w3c/wcag/pull/4906) Update affiliations  
  updated · PR · @iadawn · 💬4
- [w3c/wcag#5337](https://github.com/w3c/wcag/pull/5337) Mark up quoted note as actual note in 1.4.5 Images of Text understanding  
  updated · PR · @patrickhlauke · 💬4
- [w3c/wcag#4975](https://github.com/w3c/wcag/pull/4975) Update H91.html  
  updated · PR · @goetsu · 💬3 · Techniques
- [w3c/wcag#2629](https://github.com/w3c/wcag/issues/2629) Accessibility guidelines for front camera (navigator.getUserMedia) ?  
  updated · Issue · @tahashieenavaz · 💬2 · Discussion
- [w3c/wcag#5399](https://github.com/w3c/wcag/pull/5399) Reiterate that 4.1.2 is scoped to states/properties *that can be set by the user*  
  updated · PR · @patrickhlauke · 💬2 · Understanding, 4.1.2 Name Role Value, Substantive
- [w3c/wcag3#908](https://github.com/w3c/wcag3/issues/908) Change all occurrences of "focus"  to "keyboard focus"  
  opened · Issue · @GreggVan · 💬3
  > In looking at the latest draft we currently call focus “keyboard focus” in most places but not all - which is confusing. Checking carefully - I can't find any instance in the requirements where focus means anything other than keyboard focus. - there is no "pointer focus" other than the pointer and "hover effects" are based on pointer position - not focus. - if you click with the pointer - it moves…
- [w3c/wcag3#923](https://github.com/w3c/wcag3/pull/923) Refactors glossary to use headings instead of definition list  
  opened · PR · @adampage · 💬1
  > Resolves #870.
- [w3c/wcag3#915](https://github.com/w3c/wcag3/issues/915) “Focus retained” needs to cover more than just keyboard tabbing  
  opened · Issue · @lbeaze · 💬1 · coga, P - Focus retained
  > [Focus retained](https://w3c.github.io/wcag3/guidelines/#focus-retained) currently says “A user can focus on a [content](https://w3c.github.io/wcag3/guidelines/#dfn-content) “area”, such as a modal or popup, then resume their view of all content using a limited number of steps.” The current draft test only mentions keyboard focus. Are you planning to add test procedures for using a mouse, touchscr…
- [w3c/wcag3#917](https://github.com/w3c/wcag3/issues/917) Concerns about the exceptions in “Pointer focus indicated”  
  opened · Issue · @lbeaze · 💬1 · coga, P - Pointer focus indicated
  > The first exception is too broad. How can the provision ensure that the mechanism to un-hide the pointer indicator is not hard to use, or find, or remember, etc? We recommend explicitly stating that the indicator can be ‘un-hidden’ using a single, standard pointer movement or equivalent basic interaction requiring no memory or multi-step command. Here is a fail example: press control p and d toget…
- [w3c/wcag3#914](https://github.com/w3c/wcag3/issues/914) WCAG 3: Functional Performance Statements  
  opened · Issue · @maryjom · 💬1
  > The FPS included in WCAG 3 do not map well to the EN 301 549 (where these are Functional Performance Criteria in [V4.1.1](https://www.etsi.org/deliver/etsi_en/301500_301599/301549/04.01.01_60/en_301549v040101p.pdf)) or US Revised 508 Functional Performance Criteria. Some concerns: - How does one draw the line between "very limited" and "limited" in each of the FPS categories? The descriptions for …
- [w3c/wcag3#907](https://github.com/w3c/wcag3/pull/907) Add three exploratory sign language provisions  
  opened · PR · @iadawn · 💬1
  > Includes: * Sign language video resolution * Sign language video frame rate * Sign language speaker identified
- [w3c/wcag3#913](https://github.com/w3c/wcag3/issues/913) There should be no exception on Flashing  
  opened · Issue · @GreggVan · 💬0
  > it currently reads > No flashing over threshold > Developing > Core requirement > > Flashes are below the general flash and red flash thresholds. > > Applies when content includes flashes. > > Except when the flashing is essential. that feels like == it is safe to hit people hard over the head with glass bottle if it is essential. There may indeed be times when the right thing to do is to hit some…
- [w3c/wcag3#916](https://github.com/w3c/wcag3/issues/916) Why aren’t there any core requirements in “Expected Behavior”?  
  opened · Issue · @lbeaze · 💬0 · coga, P - Consistent control location, P - Consistent interactions, P - Conventional pattern used
  > The [“Expected behavior” guideline](https://w3c.github.io/wcag3/guidelines/#expected-behavior) has an outcome that is very important, especially for COGA users: “Users can interact with [interactive elements](https://w3c.github.io/wcag3/guidelines/#dfn-interactive-element) that behave as expected.” But the guideline currently consists of two assertions and a supplemental requirement. We are concer…
- [w3c/wcag3#918](https://github.com/w3c/wcag3/issues/918) Three concerns about “Consistent control location”  
  opened · Issue · @lbeaze · 💬0 · coga, P - Consistent control location
  > 1. Consider defining “control.” 2. Consider rewording this provision so it doesn’t apply to all kinds of “interactive elements.” (The WCAG 3 glossary for “[interactive element](https://w3c.github.io/wcag3/guidelines/#dfn-interactive-element)” lists as examples “buttons, controls, and input fields.”) 3. Consider adding a requirement or best practice to follow current platform standards for control …
- [w3c/wcag3#919](https://github.com/w3c/wcag3/issues/919) “Contextual help available” needs to factor in close proximity  
  opened · Issue · @lbeaze · 💬0 · coga, P - Contextual help available
  > The current [“contextual help available” provision](https://w3c.github.io/wcag3/guidelines/#contextual-help-available) says “[Context-sensitive help](https://w3c.github.io/wcag3/guidelines/#dfn-context-sensitive-help) is available.” This provision needs to be expanded to include visual co-location or “close proximity” of the contextual help so it’s clear to users how to proceed. This could be done…
- [w3c/wcag3#920](https://github.com/w3c/wcag3/issues/920) More info needed on the “Data visualizations” provision related to cognitive disabilities  
  opened · Issue · @lbeaze · 💬0 · coga, P - Data visualizations
  > The current editor’s draft of [Data visualizations](https://w3c.github.io/wcag3/guidelines/#data-visualizations) states that “Help is available to understand and use [data visualizations](https://w3c.github.io/wcag3/guidelines/#data-visualizations).” The provision is at the exploratory level, and an editor’s note says “Editors are considering removing this requirement.” We think it’s important to …
- [w3c/wcag3#922](https://github.com/w3c/wcag3/issues/922) “Feedback mechanism available” needs to be expanded  
  opened · Issue · @lbeaze · 💬0 · coga, P - Feedback mechanism available
  > Can the [“Feedback mechanism available” provision](https://w3c.github.io/wcag3/guidelines/#feedback-mechanism-available) be clearer about different ways users, including users with cognitive and learning disabilities, may want to provide feedback? - Anonymous feedback — this is an important option to meet privacy concerns, but it’s not the only way users may to give feedback - Feedback loops where…
- [w3c/wcag3#921](https://github.com/w3c/wcag3/issues/921) The “Support available” provision is critical and the definition of “support” needs to factor in cognitive disabilities  
  opened · Issue · @lbeaze · 💬0 · coga, P - Support available
  > COGA is glad to see the exploratory [“Support available” provision](https://w3c.github.io/wcag3/guidelines/#support-available) and is happy to help the WCAG 3 subgroup work on defining “support” to ensure this provision helps meet the needs of users with cognitive impairments. At a high level, users need to be able to: - find the support - understand how to use the support use the support (for exa…
- [w3c/wcag3#912](https://github.com/w3c/wcag3/issues/912) Auto updating text is not mentioned in WCAG 3  
  opened · Issue · @GreggVan · 💬0
  > Auto updating text does not seem to be mentioned in WCAG 3 if it is included in "visual motion" then we need to define "Visual motion" and make it clear that it is included. If it is in Pseudo motion -- then it needs to be added since that currently says "static text"
- [w3c/wcag3#911](https://github.com/w3c/wcag3/issues/911) No  WCAG3 provision  for audio that automatically plays for more than 5 sec  
  opened · Issue · @GreggVan · 💬0
  > If a page plays audio automatically when you open it -- and it is more than 5 sec and yo can't stop it --- some people using a screen reader cannot access the page since they can't hear their screen reader clearly. need a provision like "1.4.2 Audio Control Level A" "If any audio on a web page plays automatically for more than 3 seconds, either a mechanism is available to pause or stop the audio, …
- [w3c/wcag3#910](https://github.com/w3c/wcag3/issues/910) 2.4.1 Keyboard -- Keyboard Operable - is missing key parts  
  opened · Issue · @GreggVan · 💬0
  > is missing two key parts 1) it should have thins > "*without requiring specific timings for individual keystrokes, *" on the end of it so that it reads > All components on the page/view that can be operated by pointer, audio (voice or other), gesture, camera, or other means can be operated using keyboard interface only *without requiring specific timings for individual keystrokes, *. 2) it should …
- [w3c/wcag3#909](https://github.com/w3c/wcag3/issues/909) Move 2.3.3   Navigating content   down to the Keyboard Section of Inputs  
  opened · Issue · @GreggVan · 💬0
  > Move 2.3.3 Navigating content down to 2.4.1 keyboard interface input This is where all the rest of they keyboard focus and navigation is. As it is -- 2.2.3 is a bit duplicative and separated from all the other keyboard nav stuff. Note that this is all about keyboard focus not any other kind. See issue 415
- [w3c/wcag3#906](https://github.com/w3c/wcag3/issues/906) Make the provision exception structure more flexible by removing the word "when"  
  opened · Issue · @mcking65 · 💬0 · Other: Guideline Approach
  > Provisions that have exceptions are forced to use the phrasing, "except when". For example: >Content or functionality does not rely on speech alone.\ >Except when speech input is essential to the functionality. While it is possible to force any provision to use "except when" phrasing, doing so has disadvantages: 1. The temperal nature of the phrasing adds ambiguity that can make it vulnerable to i…
- [w3c/wcag3#325](https://github.com/w3c/wcag3/issues/325) Clarifying and Enhancing Requirements for Sign Language and Subtitles in WCAG 3.0  
  closed · Issue · @InfoGapBuster · 💬7 · Path: Image and media alternatives, Path: Sign language, P - Captions available (live), P - Captions available (prerecorded), P - Sign language policy (live)
- [w3c/wcag3#535](https://github.com/w3c/wcag3/issues/535) Media Alternative - What is a meaningful sound?  
  closed · Issue · @sydneycolemanfromgoogle · 💬6 · Path: Image and media alternatives, Other: Definitions & Terminology, P - Audio descriptions available (prerecorded), P - Descriptive transcripts available
- [w3c/wcag3#611](https://github.com/w3c/wcag3/issues/611) 2.1.2 Media Alternatives - Test case (and definitions)  
  closed · Issue · @JasonAment · 💬2 · Path: Image and media alternatives, P - Transcripts equivalent (prerecorded), P - Audio descriptions equivalent (prerecorded), P - Image alternatives equivalent, P - Captions equivalent (prerecorded)
- [w3c/wcag3#490](https://github.com/w3c/wcag3/issues/490) Clarify if the diacritics requirement only applies to Hebrew and Arabic  
  closed · Issue · @julierawe · 💬1 · Path: Text and wording, P - Diacritics available, Other: Internationalization
- [w3c/wcag3#172](https://github.com/w3c/wcag3/issues/172) Receiving focus is A, but removing is AAA  
  updated · Issue · @erikkroes · 💬15 · Path: Input and focus⹁ interactive components, P - Focus order meaningful
- [w3c/wcag3#186](https://github.com/w3c/wcag3/issues/186) Keyboard operation with assistive technology: 2.1.1 or 4.1.2?  
  updated · Issue · @JAWS-test · 💬12 · Path: Input and focus⹁ interactive components, P - Keyboard operable
- [w3c/wcag3#185](https://github.com/w3c/wcag3/issues/185) Proposal for a new SC for hover (WCAG 3.0)  
  updated · Issue · @JAWS-test · 💬6 · Path: Input and focus⹁ interactive components, P - Pointer focus indicated
- [w3c/wcag3#540](https://github.com/w3c/wcag3/issues/540) Speech and voice input - Real-time text available  
  updated · Issue · @sydneycolemanfromgoogle · 💬3 · Path: Input and focus⹁ interactive components, P - Real-time text available
- [w3c/wcag3#891](https://github.com/w3c/wcag3/pull/891) Revise glossary reference in relationships-detectable to use the term "programmatically detectable"  
  updated · PR · @mcking65 · 💬3 · P - Relationships detectable
- [w3c/wcag3#616](https://github.com/w3c/wcag3/issues/616) Focus placed should be a core requirement  
  updated · Issue · @ajsaucier · 💬2 · Path: Input and focus⹁ interactive components, P - Focus retained, P - Focus placed
- [w3c/wcag3#76](https://github.com/w3c/wcag3/issues/76) Input control - needs clarification  
  updated · Issue · @KevinP-NZ · 💬2 · Path: Input and focus⹁ interactive components, P - Input method flexible
- [w3c/wcag3#157](https://github.com/w3c/wcag3/issues/157) Clarifying No Keyboard Traps (SC 2.1.2)  
  updated · Issue · @njeleniauskas · 💬2 · Path: Input and focus⹁ interactive components, P - No keyboard traps
- [w3c/wcag3#902](https://github.com/w3c/wcag3/pull/902) Move accessibility supported to a new testing section and recast it as user agent supported  
  updated · PR · @mcking65 · 💬2
- [w3c/wcag3#622](https://github.com/w3c/wcag3/issues/622) Add explicit requirement for Scrollable regions to be included in keyboard tab order  
  updated · Issue · @DaleenRabe · 💬1 · Path: Input and focus⹁ interactive components, P - Focus relevant
- [w3c/wcag3#701](https://github.com/w3c/wcag3/pull/701) Multi-step process provisions  
  updated · PR · @giacomo-petri · 💬1
- [w3c/wcag3#73](https://github.com/w3c/wcag3/issues/73) Image and media alternatives - Clear labelling  
  updated · Issue · @KevinP-NZ · 💬1 · Path: Image and media alternatives, P - Transcripts findable
- [w3c/wcag3#520](https://github.com/w3c/wcag3/issues/520) [Sounds Identified]: contradicts “transcripts available”?  
  updated · Issue · @sydneycolemanfromgoogle · 💬1 · Path: Image and media alternatives, P - Sounds identified in transcripts
- [w3c/wcag3#268](https://github.com/w3c/wcag3/issues/268) Requirements: Voice Control  
  updated · Issue · @alastc · 💬0 · Path: Input and focus⹁ interactive components, Requirement tracking, P - Speech not relied on
- [w3c/wcag3#92](https://github.com/w3c/wcag3/issues/92) Outcome for bypass bocks  
  updated · Issue · @detlevhfischer · 💬0 · Path: Input and focus⹁ interactive components, P - Focus relevant, P - Focus movement relevant
- [w3c/wcag3#820](https://github.com/w3c/wcag3/issues/820) Input method versus input modality  
  updated · Issue · @adampage · 💬0 · Path: Input and focus⹁ interactive components, Other: Definitions & Terminology, P - Input method flexible
- [w3c/wcag3#874](https://github.com/w3c/wcag3/issues/874) AFixt Comments on WCAG 3 draft as of 10 September 2026  
  updated · Issue · @karlgroves · 💬0 · Conformance, accessibility supported
- [w3c/wcag2ict#997](https://github.com/w3c/wcag2ict/pull/997) Tidy up note at start of comments on level AAA  
  merged · PR · @pday1 · 💬1
  > As per issue https://github.com/w3c/wcag2ict/issues/989 and TF meeting of https://www.w3.org/2026/09/17-wcag2ict-minutes.html#e098 Converted editor's note to regular note. Added introductory sentence. Moved note after the 2 sections quoted from WCAG 2.2
- [w3c/wcag2ict#978](https://github.com/w3c/wcag2ict/issues/978) AG WG Review: 2.4.13 Focus Appearance (Level AAA) WCAG2ICT Guidance  
  updated · Issue · @pday1 · 💬5 · Please Review
- [w3c/wcag2ict#1004](https://github.com/w3c/wcag2ict/pull/1004) Editorial issues arising from AG WG review of AAA content  
  updated · PR · @pday1 · 💬1 · Editorial
- [act-rules/act-rules.github.io#2436](https://github.com/act-rules/act-rules.github.io/pull/2436) Chore: prettier formatting in CI  
  merged · PR · @daniel-montalvo · 💬3
  > This moves prettier formatting to CI and removes existing pre-commit hooks to ensure prettier always runs on PRs and not just when someone commits with deps installed on their local machine.
- [act-rules/act-rules.github.io#2462](https://github.com/act-rules/act-rules.github.io/pull/2462) Add a skill for publishing one ACT rule  
  opened · PR · @WilcoFiers · 💬2
  > Add a skill that drafts a WAI changelog and a one-paragraph AGWG pull-request body for a single ACT rule, then runs `approve-rule` only after that text is explicitly accepted. Closes issue(s): - none Need for Call for Review: This will not require a Call for Review: this adds agent instructions under `.agents/skills/publish-act-rule/` and does not change a rule, definition, or test outcome. --- ##…
- [act-rules/act-rules.github.io#2463](https://github.com/act-rules/act-rules.github.io/issues/2463) Come up with an AI policy  
  opened · Issue · @WilcoFiers · 💬0
  > Notes from today's CG call: ## AI use within ACT CG 1. Issues / comments / reviews / PRs written by AI should disclose that they were written by AI. - Disclosed it was used - You reviewed, understand & agree with the content - The content is concise, 2. AI written rules & examples - Public policy - Content verified by humans ## AI use for implementation To be discussed: - AI created rules - Labell…
- [act-rules/act-rules.github.io#2461](https://github.com/act-rules/act-rules.github.io/issues/2461) Text nodes and allowed accessibility child roles  
  opened · Issue · @giacomo-petri · 💬0 · Rule Update, Agenda item, WAI-ARIA 1.3
  > The ARIA WG opened [aria#2929](https://github.com/w3c/aria/pull/2929) to clarify how text nodes affect the determination of allowed accessibility children. The [ARIA required owned elements rule](https://www.w3.org/WAI/standards-guidelines/act/rules/bc4a75/proposed/) currently uses ARIA 1.2 terminology (required owned elements), which will need to be updated as part of the alignment with ARIA 1.3.…
- [act-rules/act-rules.github.io#2425](https://github.com/act-rules/act-rules.github.io/pull/2425) ACT 2.4.6 Heading descriptive rule update  
  updated · PR · @grifare · 💬6
- [act-rules/act-rules.github.io#2458](https://github.com/act-rules/act-rules.github.io/pull/2458) Bump moment from 2.30.1 to 2.31.0  
  updated · PR · @dependabot[bot] · 💬1 · dependencies, javascript

### ARIA WG

- [w3c/aria#2935](https://github.com/w3c/aria/pull/2935) Chore: Remove duplicate  
  merged · PR · @daniel-montalvo · 💬2
- [w3c/aria#2934](https://github.com/w3c/aria/pull/2934) Editorial: Fix some minor typos in process document  
  merged · PR · @daniel-montalvo · 💬2 · editorial
  > Some typos and style guide issues. I'll put my proposed updates (more significant) in another PR once we land this one.
- [w3c/aria#2932](https://github.com/w3c/aria/pull/2932) Chore: Removes obsolete call in ariaChild.js  
  merged · PR · @daniel-montalvo · 💬2
  > 🚀 **Netlify Preview**: 🔄 **this PR updates the following specs**: - [ARIA preview](https://deploy-preview-2932--wai-aria.netlify.app/index.html) &mdash; [ARIA diff](https://services.w3.org/htmldiff?doc1=https%3A%2F%2Fw3c.github.io%2Faria%2F&doc2=https%3A%2F%2Fdeploy-preview-2932--wai-aria.netlify.app%2Findex.html) Based on my work in #2928, I found that `npx respec -s dpub-aria/index.html -o dpub-…
- [w3c/aria#2945](https://github.com/w3c/aria/pull/2945) HTML-AAM: Map image maps to ATK_ROLE_IMAGE_MAP  
  opened · PR · @KateZhaoTR · 💬2 · spec:html-aam
  > 🚀 **Netlify Preview**: 🔄 **this PR updates the following specs**: - [html-aam preview](https://deploy-preview-2945--wai-aria.netlify.app/html-aam/index.html) &mdash; [html-aam diff](https://services.w3.org/htmldiff?doc1=https%3A%2F%2Fw3c.github.io%2Fhtml-aam%2F&doc2=https%3A%2F%2Fdeploy-preview-2945--wai-aria.netlify.app%2Fhtml-aam%2Findex.html) Closes [#614](https://github.com/w3c/html-aam/issues…
- [w3c/aria#2941](https://github.com/w3c/aria/pull/2941) Chore: Try wpt referencing from within respec  
  opened · PR · @daniel-montalvo · 💬2 · spec:html-aam
  > 🚀 **Netlify Preview**: 🔄 **this PR updates the following specs**: - [html-aam preview](https://deploy-preview-2941--wai-aria.netlify.app/html-aam/index.html) &mdash; [html-aam diff](https://services.w3.org/htmldiff?doc1=https%3A%2F%2Fw3c.github.io%2Fhtml-aam%2F&doc2=https%3A%2F%2Fdeploy-preview-2941--wai-aria.netlify.app%2Fhtml-aam%2Findex.html) For Editors discussion -- includes references to a W…
- [w3c/aria#2942](https://github.com/w3c/aria/pull/2942) Editorial: clarify "list" as "list of roles" in Allowed Accessibility Child roles  
  opened · PR · @jnurthen · 💬2 · spec:aria
  > 🚀 **Netlify Preview**: 🔄 **this PR updates the following specs**: - [ARIA preview](https://deploy-preview-2942--wai-aria.netlify.app/index.html) &mdash; [ARIA diff](https://services.w3.org/htmldiff?doc1=https%3A%2F%2Fw3c.github.io%2Faria%2F&doc2=https%3A%2F%2Fdeploy-preview-2942--wai-aria.netlify.app%2Findex.html) Closes #2939 In [Allowed Accessibility Child Roles](https://w3c.github.io/aria/#must…
- [w3c/aria#2939](https://github.com/w3c/aria/issues/2939) too many uses of "list" in 5.2.6  
  opened · Issue · @pkra · 💬1 · editorial
  > Via #2930, from today's call. 5.2.6 uses "list" to refer to the list of allowed child roles but also gives role=list as example. This is confusing. Some re-organization should sort it out.
- [w3c/aria#2938](https://github.com/w3c/aria/issues/2938) updating the language in Section 7 (Accessibility Tree) beyond DOM nodes  
  opened · Issue · @pkra · 💬1 · question, Agenda
  > The wording in Section 7 only ever speaks about DOM nodes. In particular in the definitions for accessibility child/parent/etc. CSS now generates complex accessibility tree structures (i.e. more than text nodes) e.g. https://github.com/w3c/css-aam/issues/18. While we still might not be able to specify the accessibility tree, this may lead to problems we might want to fix.
- [w3c/aria#2946](https://github.com/w3c/aria/issues/2946) Inappropriate example in Text Equivalent Computation 2.1.2  
  opened · Issue · @neet · 💬0
  > # Describe your concern Step 2.1 of text equivalent computation says > - 2.1 Hidden Not Referenced: If the current node is [hidden](https://www.w3.org/TR/wai-aria/#dfn-hidden) and is: > - 2.1.1 Not part of an aria-labelledby or aria-describedby traversal, where the node directly referenced by that relation was hidden. > - 2.1.2 Nor part of a native host language text alternative [element](https://…
- [w3c/aria#2940](https://github.com/w3c/aria/issues/2940) Explore (and potentially improve) respec wpt test implementation  
  opened · Issue · @daniel-montalvo · 💬0
  > Currently [bikeshed](https://speced.github.io/bikeshed/#testing) allows to reference a WPT file from within a testable assertion on a given spec. According to [respec documentation](https://respec.org/docs/#data-tests) that's also possible. Opening this issue to: * try this out and see if it works (MVP at least) for the ARIA suite #2941 * brainstorm more ideas around WPT integration for respec tha…
- [w3c/aria#2944](https://github.com/w3c/aria/issues/2944) Artifact positional semantics  
  opened · Issue · @DuffJohnson · 💬0
  > This issue is raised in conjunction with development of [W3C’s PDF-AAM](https://www.w3.org/WAI/about/groups/task-forces/pdf-aam/). # Use case Documents can include content that may not be relevant to readers depending on the nature of their engagement. In PDF this class of content is known as “artifact”. There are two types of artifacts in PDF. This proposal only discusses the **Artifact** structu…
- [w3c/aria#2943](https://github.com/w3c/aria/issues/2943) Title content (not metadata)  
  opened · Issue · @DuffJohnson · 💬0 · spec:pdf-aam
  > This issue is raised in conjunction with development of [W3C’s PDF-AAM](https://www.w3.org/WAI/about/groups/task-forces/pdf-aam/). # Use case Documents (more so than web pages) frequently include so-called [front-matter or prelim](https://www.scribendi.com/academy/articles/front_matter.en.html) content that logically precedes the main body of the content. A very common subset of front matter is ti…
- [w3c/aria#2912](https://github.com/w3c/aria/issues/2912) ARIA content model  
  closed · Issue · @pkra · 💬1 · F2FCandidate
- [w3c/aria#1708](https://github.com/w3c/aria/issues/1708) tracking issue for <dialog> & role=dialog  
  updated · Issue · @jnurthen · 💬16 · Agenda
- [w3c/aria#2483](https://github.com/w3c/aria/pull/2483) Clarify Accessibility Parent-Child Relationships for menu, group, and menuitem  
  updated · PR · @giacomo-petri · 💬14 · Agenda, clarification, spec:aria
- [w3c/aria#2036](https://github.com/w3c/aria/issues/2036) Interactive Lists  
  updated · Issue · @MarioBatusic · 💬11 · F2FCandidate, feature
- [w3c/aria#2863](https://github.com/w3c/aria/pull/2863) Update a no href to map to link role  
  updated · PR · @lolaodelola · 💬10 · Agenda, spec:html-aam
- [w3c/aria#2800](https://github.com/w3c/aria/pull/2800) Core-AAM: Add Computed Accessibility Properties section  
  updated · PR · @spectranaut · 💬8 · spec:core-aam
- [w3c/aria#2919](https://github.com/w3c/aria/pull/2919) Clarify setSize and posinSet calculation for radios  
  updated · PR · @spectranaut · 💬8 · spec:core-aam, spec:html-aam
- [w3c/aria#2929](https://github.com/w3c/aria/pull/2929) clarification: text nodes and allowed accessibility child roles  
  updated · PR · @pkra · 💬6 · clarification, spec:aria, needs ACT review
- [w3c/aria#1331](https://github.com/w3c/aria/issues/1331) FPWD of ARIA 1.3  
  updated · Issue · @jnurthen · 💬5 · editorial
- [w3c/aria#2501](https://github.com/w3c/aria/issues/2501) continue aria.js work  
  updated · Issue · @pkra · 💬5 · editorial
- [w3c/aria#2914](https://github.com/w3c/aria/pull/2914) Editorial: Security considerations (from 2869)  
  updated · PR · @daniel-montalvo · 💬4 · spec:aria
- [w3c/aria#2925](https://github.com/w3c/aria/issues/2925) "API's focus event" is ambiguous  
  updated · Issue · @cookiecrook · 💬4
- [w3c/aria#2904](https://github.com/w3c/aria/issues/2904) review use of "label" (as a standalone word)  
  updated · Issue · @pkra · 💬4 · editorial
- [w3c/aria#2930](https://github.com/w3c/aria/issues/2930) Clarify "Allowed Accessibility Child Roles"  
  updated · Issue · @gsnedders · 💬3 · Agenda
- [w3c/aria#2928](https://github.com/w3c/aria/pull/2928) Chore: Enable stricter tooling -- enable respec validator and some specprod validators  
  updated · PR · @daniel-montalvo · 💬3
- [w3c/aria#2931](https://github.com/w3c/aria/pull/2931) Update browser_accessibility_heuristics.md  
  updated · PR · @cookiecrook · 💬3
- [w3c/aria#2883](https://github.com/w3c/aria/issues/2883) aria-actions on a non-focusable ancestor behavior on descendants is undefined  
  updated · Issue · @cookiecrook · 💬3 · F2FCandidate
- [w3c/aria#2926](https://github.com/w3c/aria/issues/2926) role="time" lacks disambiguation (time vs. date vs. duration) for platform TTS APIs  
  updated · Issue · @dtsengchromium · 💬1
- [w3c/aria#2903](https://github.com/w3c/aria/issues/2903) F2F: WPT Accessibility Updates Session in the ARIA WG TPAC schedule  
  updated · Issue · @cookiecrook · 💬1 · F2FCandidate
- [w3c/aria-practices#3474](https://github.com/w3c/aria-practices/pull/3474) [For preview] Accordion Example: Animate expand and collapse unless reduced motion is preferred  
  opened · PR · @daniel-montalvo · 💬0
  > ___ [WAI Preview Link](https://deploy-preview-487--aria-practices.netlify.app/ARIA/apg) _(Last built on Wed, 14 Oct 2026 16:57:40 GMT)._
- [w3c/aria-practices#3473](https://github.com/w3c/aria-practices/pull/3473) Accordion Example: Animate expand and collapse unless reduced motion is preferred  
  updated · PR · @jsabutis · 💬2
- [w3c/core-aam#272](https://github.com/w3c/core-aam/issues/272) aria-keyshortcuts: define macOS mapping of Meta/Alt to Command/Option in AXKeyShortcutsValue  
  opened · Issue · @petdud · 💬7
  > The aria-keyshortcuts syntax uses platform-neutral modifier names (Meta, Alt). On macOS these correspond to the Command and Option keys, but the macOS mapping in Core-AAM (https://w3c.github.io/aria/core-aam/#ariaKeyshortcuts) does not say whether browsers should translate them for AXKeyShortcutsValue. Result: VoiceOver announces "Meta Shift M" / "Alt Shift M" in Firefox and Chromium, while Apple …
- [w3c/core-aam#270](https://github.com/w3c/core-aam/issues/270) aria-checked on option: how to expose in AX API?  
  updated · Issue · @spectranaut · 💬7 · agenda
- [w3c/core-aam#271](https://github.com/w3c/core-aam/issues/271) Clarify "option inside combobox" vs. "option not inside combobox"  
  updated · Issue · @dtsengchromium · 💬2
- [w3c/html-aam#616](https://github.com/w3c/html-aam/issues/616) Clarify mapping of multiple on <select multiple size="1"> (rendered as a drop-down box)  
  opened · Issue · @dtsengchromium · 💬2 · Agenda
  > In HTML (and in Chromium/WebKit), `<select multiple size="1">` renders as a drop-down box (a button that opens a popup menu/list of options) rather than an in-page list box: ``` data:text/html,<select size=1 multiple><option>apple</option><option>banana</option></select> ``` HTML-AAM already distinguishes between `<select>` rendered as a list box (3.5.115, mapped to listbox) and `<select>` rendere…
- [w3c/html-aam#617](https://github.com/w3c/html-aam/issues/617) Consider mapping the form attribute on form-associated elements to a relationship  
  opened · Issue · @dtsengchromium · 💬1 · Agenda
  > In HTML-AAM 3.6.52 (https://w3c.github.io/html-aam/#att-form), the form attribute on form-associated elements (button, fieldset, input, label, object, output, select, textarea, and form-associated custom elements) is currently "Not mapped" across all platforms. However, there is a common real-world pattern—especially on mobile e-commerce sites such as Shopify—where a `<form>` and its submit/checko…
- [w3c/html-aam#620](https://github.com/w3c/html-aam/issues/620) Add AXRoleDescription mapping for <output>  
  opened · Issue · @neet · 💬0
  > When we considered introducing an UI component that uses `<output>` element to our design system, we noticed that the announcement for the element becomes "{content}, output" only on VoiceOver + Safari. After investigation, we identified that this is because Safari sets "output" (or a corresponding localised string) to `AXRoleDescription`. This behaviour seems to be intentionally introduced to Web…
- [w3c/html-aam#619](https://github.com/w3c/html-aam/issues/619) Are there potential mappings for anchor rel values?  
  opened · Issue · @pkra · 💬0
  > Inspired by #613, I'm wondering if AAPIs might be able to make use of some `rel` attribute values on `a` elements. The [HTML spec's link type list](https://html.spec.whatwg.org/multipage/links.html#linkTypes) is fairly small (for `a`) and potentially useful values might be fewer still. But e.g. `external` could help identify external links programmatically (and more reliably than AT heuristics aro…
- [w3c/html-aam#618](https://github.com/w3c/html-aam/issues/618) Add Proposed Video Poster Element to HTML Accessibility API Mappings  
  opened · Issue · @scottjehl · 💬0
  > # Description of feature request This is a proposal to add the proposed HTML video `<poster>` element to the HTML Accessibility API Mappings. The `<poster>` element will bring `<img>` element capabilities to HTML `<video>` poster images, including responsive image selection and accessible description of the poster frame. HTML Spec Proposal: https://github.com/whatwg/html/pull/12585 ## Poster Image…
- [w3c/html-aam#613](https://github.com/w3c/html-aam/issues/613) [HTML-AAM] IA2 and ATK should have a valid mapping for 3.6.138 attr-target  
  updated · Issue · @kyraseevers · 💬4 · good first issue
- [w3c/html-aam#614](https://github.com/w3c/html-aam/issues/614) image maps should be exposed as ATK_ROLE_IMAGE_MAP; not ATK_ROLE_IMAGE  
  updated · Issue · @joanmarie · 💬2 · good first issue
- [w3c/html-aam#615](https://github.com/w3c/html-aam/issues/615) Restructuring wpt/html-aam directory  
  updated · Issue · @rahimabdi · 💬1
- [w3c/html-aria#608](https://github.com/w3c/html-aria/issues/608) Add Proposed Video Poster Element to the ARIA in HTML Specification  
  opened · Issue · @scottjehl · 💬1
  > # Description of feature request This is a proposal to add the proposed HTML video `<poster>` element to the ARIA in HTML spec. The <poster> element will bring <img> element capabilities to HTML <video> poster images, including responsive image selection and accessible description of the poster frame. HTML Spec Proposal: https://github.com/whatwg/html/pull/12585 This is a complementary feature req…
- [w3c/html-aria#609](https://github.com/w3c/html-aria/issues/609) <mark> has an implicit role `mark`  
  opened · Issue · @neet · 💬0
  > In the latest ARIA in HTML, it is documented that `<mark>` element has no implicit ARIA role https://github.com/w3c/html-aria/blob/9fd6a745b6be74dc17d24197ba3cf9c056f12e81/index.html#L2178-L2183 However in the HTML-AAM 1.0, corresponding ARIA role for `<mark>` is written as `mark` https://github.com/w3c/aria/blob/8bf52aad22aa15e0fac28e9bfeb950d1c23dc65a/html-aam/index.html#L5006-L5009 I think we s…
- [w3c/html-aria#561](https://github.com/w3c/html-aria/issues/561) replace "required owned elements" with "Allowed Child Elements"  
  updated · Issue · @pkra · 💬1
- [w3c/aria-at#1419](https://github.com/w3c-cg/aria-at/pull/1419) Add HTML Anchor Element with href Test Plan  
  opened · PR · @mehm8128 · 💬0
  > [Preview Tests](https://deploy-preview-1419--aria-at.netlify.app) Add a new test plan for an HTML `a` element with the `href` attribute (`tests/html/href-a`), modeled on the HTML button and disabled button test plans. ## Tests | Test | Setup | Assertions | |---|---|---| | Navigate forwards to a link | focus on the link before | role `link`, name "W3C website" | | Navigate backwards to a link | foc…
- [w3c/aria-at#1418](https://github.com/w3c-cg/aria-at/pull/1418) Bump @simple-git/argv-parser and simple-git  
  opened · PR · @dependabot[bot] · 💬0 · dependencies, javascript
  > [Preview Tests](https://deploy-preview-1418--aria-at.netlify.app) Bumps [@simple-git/argv-parser](https://github.com/steveukx/git-js/tree/HEAD/packages/argv-parser) to 2.0.1 and updates ancestor dependency [simple-git](https://github.com/steveukx/git-js/tree/HEAD/simple-git). These dependencies need to be updated together. Updates `@simple-git/argv-parser` from 1.1.1 to 2.0.1 <details> <summary>Re…
- [w3c/aria-at#1420](https://github.com/w3c-cg/aria-at/issues/1420) Intro video not found  
  closed · Issue · @AnGabSS · 💬2 · bug
- [w3c/aria-at#1417](https://github.com/w3c-cg/aria-at/pull/1417) Bump simple-git from 3.36.0 to 4.0.1  
  closed · PR · @dependabot[bot] · 💬1 · dependencies, javascript
- [w3c/aria-at#163](https://github.com/w3c-cg/aria-at/pull/163) WIP: Add sample name structure and wire up with test running and review files  
  closed · PR · @mfairchild365 · 💬0
- [w3c/aria-at#1415](https://github.com/w3c-cg/aria-at/issues/1415) NVDA doesn't announce the correct role and state of a disabled button on using INSERT + TAB in browse mode on.  
  updated · Issue · @AmruthRaj-David · 💬2

### APA / 水平レビュー

- [w3c/a11y-request#192](https://github.com/w3c/a11y-request/issues/192) Spec_name YYYY-MM-DD  
  opened · Issue · @Nilopa9 · 💬0 · SR, WD, REVIEW REQUESTED, pending, s:-
  > We have conducted a self-review of our spec [SPEC_NAME_HERE](URL_GOES_HERE), and the results can be found at URL_FOR_THE_ISSUE_IN_YOUR_REPO. Please check our findings. - name of spec to be reviewed: - shortname: - URL of spec: - Do you need a reply by a particular date? Other comments:
- [w3c/a11y-request#191](https://github.com/w3c/a11y-request/issues/191) Global Privacy Control 2026-10-15 > 2026-12-26  
  opened · Issue · @AramZS · 💬0 · LC, REVIEW REQUESTED, pending, s:GPC
  > In the issue title above add the document name followed by the date of this request, then the date of your proposed deadline for comments. - name of spec to be reviewed: Global Privacy Control - shortname: GPC - URL of spec: https://www.w3.org/TR/2026/WD-gpc-20260924/ - What and when is your next expected transition? Candidate Recommendation, currently in wide review process - What has changed sin…
- [w3c/a11y-request#163](https://github.com/w3c/a11y-request/issues/163) Digital Credentials 2026-05-14 > 2026-07-14  
  updated · Issue · @marcoscaceres · 💬5 · LC, REVIEW REQUESTED, s:digital-credentials/
- [w3c/csswg-drafts#14316](https://github.com/w3c/csswg-drafts/issues/14316) [css-forms-1] Use empty alt text for ::picker-icon and ::checkmark  
  updated · Issue · @fantasai · 💬16 · css-forms-1, Needs Edits, a11y-tracker, Needs Testcase (WPT)
- [w3c/csswg-drafts#12269](https://github.com/w3c/csswg-drafts/issues/12269) [css-overflow-5]: mechanism to override and set semantic props on overflow markers and buttons  
  updated · Issue · @smhigley · 💬7 · i18n-tracker, a11y-tracker, css-overflow-5

### WHATWG

- [whatwg/html#13068](https://github.com/whatwg/html/issues/13068) Media element attributes resolve against the fragment parser's inert document's base URL  
  opened · Issue · @noamr · 💬0 · topic: media
  > The HTML fragment parsing algorithm creates elements in an inert Document (base URL about:blank) and only adopts them into the target's node document on insertion. Three attributes resolve their URL eagerly, against the node document at the time the attribute is set, and never re-resolve on adoption: media src — resource selection, "relative to the media element's node document when the src attrib…
- [whatwg/html#13070](https://github.com/whatwg/html/pull/13070) Editorial: fix undefined variable when creating a Document  
  opened · PR · @shannonbooth · 💬0
  > *** <a href="https://whatpr.org/html/13070/document-lifecycle.html" title="Last updated on Oct 13, 2026, 10:02 PM UTC (023efa7)">/document-lifecycle.html</a> ( <a href="https://whatpr.org/html/13070/98753fa...023efa7/document-lifecycle.html" title="Last updated on Oct 13, 2026, 10:02 PM UTC (023efa7)">diff</a> )
- [whatwg/html#12560](https://github.com/whatwg/html/issues/12560) Nodes are made non-inert before sanitizing  
  closed · Issue · @zcorpan · 💬3 · topic: sanitizer
- [whatwg/html#11723](https://github.com/whatwg/html/pull/11723) [focusgroup] Add the focusgroup attribute   
  updated · PR · @janewman · 💬14
- [whatwg/html#12590](https://github.com/whatwg/html/pull/12590) [draft] Spell check custom dictionary  
  updated · PR · @bkardell · 💬5 · addition/proposal, needs implementer interest, i18n-tracker, needs tests, a11y-tracker
- [whatwg/html#13051](https://github.com/whatwg/html/issues/13051) Proposal: Expose sequential focus navigation primitives  
  updated · Issue · @vmpstr · 💬2 · addition/proposal, needs implementer interest
- [whatwg/html#12596](https://github.com/whatwg/html/issues/12596) Scrolling to a fragment should have consistent focus handling  
  updated · Issue · @Th3S4mur41 · 💬1 · topic: navigation, topic: focus
- [whatwg/html#13050](https://github.com/whatwg/html/pull/13050) Add the focusreset event  
  updated · PR · @noamr · 💬1

### ブラウザ / AT

- [web-platform-tests/interop-accessibility#254](https://github.com/web-platform-tests/interop-accessibility/issues/254) `aamtest`: Write tests for Core-AAM - ATSPI  
  opened · Issue · @spectranaut · 💬0 · aamtest
  > Finish test coverage for [events](https://w3c.github.io/aria/core-aam/#mapping_events_state-change) -- https://github.com/web-platform-tests/wpt/tree/master/core-aam/aamtests/event
- [web-platform-tests/interop-accessibility#251](https://github.com/web-platform-tests/interop-accessibility/issues/251) `aamtest`: Write tests for Core-AAM - UIA  
  opened · Issue · @spectranaut · 💬0 · aamtest
  > @hatheo started this work for the role tests: https://github.com/web-platform-tests/wpt/pull/60504 Remaining work: - [ ] tests for states and attributes (https://github.com/web-platform-tests/wpt/tree/master/core-aam/aamtests/attribute) - [ ] tests for [events](https://w3c.github.io/aria/core-aam/#mapping_events_state-change) -- https://github.com/web-platform-tests/wpt/tree/master/core-aam/aamtes…
- [web-platform-tests/interop-accessibility#252](https://github.com/web-platform-tests/interop-accessibility/issues/252) `aamtest`: Write tests for Core-AAM - AX API  
  opened · Issue · @spectranaut · 💬0 · aamtest
  > Write tests for: - [ ] add AX API role mapping test (https://github.com/web-platform-tests/wpt/tree/master/core-aam/aamtests/role) - [ ] add AX API state and attribute mapping tests (https://github.com/web-platform-tests/wpt/tree/master/core-aam/aamtests/attribute) - [ ] tests for [events](https://w3c.github.io/aria/core-aam/#mapping_events_state-change) -- https://github.com/web-platform-tests/wp…
- [web-platform-tests/interop-accessibility#253](https://github.com/web-platform-tests/interop-accessibility/issues/253) `aamtest`: Write tests for Core-AAM - IA2  
  opened · Issue · @spectranaut · 💬0 · aamtest
  > Write tests for: - [ ] add IA2/MSAA role mapping test (https://github.com/web-platform-tests/wpt/tree/master/core-aam/aamtests/role) - [ ] add IA2/MSAA state and attribute mapping tests (https://github.com/web-platform-tests/wpt/tree/master/core-aam/aamtests/attribute) - [ ] tests for [events](https://w3c.github.io/aria/core-aam/#mapping_events_state-change) -- https://github.com/web-platform-test…
- [web-platform-tests/interop-accessibility#255](https://github.com/web-platform-tests/interop-accessibility/issues/255) `aamtest`: How to test HTML-AAM concepts that map to Core-AAM?  
  opened · Issue · @spectranaut · 💬0 · aamtest
  > Many HTML-AAM concepts map directly to aria roles and/or states - for example, [the `a` tag](https://w3c.github.io/aria/html-aam/#el-a) maps to the [role=link](https://w3c.github.io/aria/core-aam/#role-map-link). Here is the Core-AAM test for role link: https://github.com/web-platform-tests/wpt/blob/master/core-aam/aamtests/role/link.py Consider refactoring how we write the core-aam tests, since o…
- [web-platform-tests/interop-accessibility#250](https://github.com/web-platform-tests/interop-accessibility/issues/250) Write tests for CSS generated content with alt text (::before/::after and ::marker)  
  opened · Issue · @zcorpan · 💬0 · Agenda+
  > See https://github.com/w3c/accname/issues/253
- [web-platform-tests/interop-accessibility#229](https://github.com/web-platform-tests/interop-accessibility/issues/229) `aamtest` possible improvements: parameterized wpt runs by accessibility API (for windows)  
  updated · Issue · @spectranaut · 💬0 · aamtest
- [web-platform-tests/interop-accessibility#230](https://github.com/web-platform-tests/interop-accessibility/issues/230) `aamtest` possible improvements: Report "PRECONDITION_FAILED" instead of missing for test on wrong platform  
  updated · Issue · @spectranaut · 💬0 · aamtest

## 2. 議事録

- 2026-10-12 COGA TF: https://www.w3.org/2026/10/12-coga-minutes.html
- 2026-10-13 AGWG: https://www.w3.org/2026/10/13-ag-minutes.html
- 2026-10-14 ARIA APG TF: https://www.w3.org/2026/10/14-aria-apg-minutes.html
- 2026-10-14 APA WG: https://www.w3.org/2026/10/14-apa-minutes.html
- 2026-10-15 ARIA WG: https://www.w3.org/2026/10/15-aria-minutes.html

## 3. フィード

(なし)

## 4. リリース

- [nvaccess/nvda release-2026.3beta5](https://github.com/nvaccess/nvda/releases/tag/release-2026.3beta5) (pre) (2026-10-14)  
  * Highlights can be found in the [release blog post](https://www.nvaccess.org/post/nvda-2026-3beta5/). * [VirusTotal scan results](https://www.virustotal.com/gui/file-analysis/NjNhNDg2MGI5MTNmZDI3MjQ0MzViY2MzMmZhYjc2OGE6MTc5MTk1NTg0Nw==/detection) * SHA256 sum: `c1d2cc7bc21126a224fdc0733fef5f20adf21
- [GoogleChrome/modern-web-guidance v0.0.194](https://github.com/GoogleChrome/modern-web-guidance/releases/tag/v0.0.194) (2026-10-12)  
  * Introduced a new guide for **[slider](https://github.com/GoogleChrome/modern-web-guidance/blob/v0.0.194/skills/modern-web-guidance/guides/forms/slider.md)** covering best practices for building accessible, custom-styled range inputs for numeric value selection. * Introduced a new guide for **[swit

## 5. 新規リポジトリ

- [fauzulkc/circle-lens](https://github.com/fauzulkc/circle-lens) ★29 Go — A free screen magnifier that opens where you're looking: draw a circle twice with the mouse. For Windows, your browser, and your website (npm circle-lens).  
  topics: a11y, accessibility, browser-extension, chrome-extension, firefox-addon, golang, javascript, low-vision
- [ynotdraw/slab-elements](https://github.com/ynotdraw/slab-elements) ★19 TypeScript — Headless Web Components built on native elements. Bring your own design.  
  topics: a11y, aria, base-ui, custom-elements, customelements, design-system, headless, headlessui
- [Protonpopatch/over-the-hill-camera-motion-profile-helper](https://github.com/Protonpopatch/over-the-hill-camera-motion-profile-helper) ★16  — Windows utility for over the hill focused on camera movement, camera motion, and camera profile.  
  topics: 2026, accessibility, camera, comfort, game-tools, gaming-utility, motion, over-the-hill
- [A-l-an/FocalFlow](https://github.com/A-l-an/FocalFlow) ★16 Java — FocalFlow research prototype: Android accessibility client and Python AI backend for task-oriented mobile interaction.  
  topics: 
- [kerstz/JizzCraft](https://github.com/kerstz/JizzCraft) ★14 Rust — Private, offline library and player for your own adult collection. Rust, egui, GStreamer, SQLite. No account, no telemetry. Linux, 18+.  
  topics: accessibility, cli, desktop-app, egui, gstreamer, image-viewer, keyboard-driven, linux
- [Greyland-Fireworks/audhd-ui-guide](https://github.com/Greyland-Fireworks/audhd-ui-guide) ★8  — Practical guidance for AuDHD-friendly interfaces that are easier to understand, use, pause, resume and correct for users and developers who face the combined challenges of Autism and ADHD.  
  topics: accessibility, accessibility-analysis, accessibility-tools, adhd-aid, adhd-friendly, ai-agents, ai-agents-and-tools, ai-agents-mcp
- [Adilmunawar/ARGUS](https://github.com/Adilmunawar/ARGUS) ★8 JavaScript — Open source sovereign private cloud blueprint that replaces AWS on hardware you own. Windows Server, Hyper V, Service Fabric, GitOps and zero trust security, with 34 architecture decisions, runbooks, …  
  topics: accessibility, active-directory, architecture-decision-records, aws-alternative, cloud-migration, devops, disaster-recovery, dotnet
- [gaurabh-pei/nogrammerly](https://github.com/gaurabh-pei/nogrammerly) ★7 Swift — The free, open-source, on-device Grammarly alternative for Mac and Windows. Spelling, grammar, tone checks and rewrites in Slack, Teams, Outlook, Mail & Zoom — powered by Apple Intelligence and Window…  
  topics: accessibility, apple-intelligence, copilot-plus-pc, csharp, foundation-models, grammar-checker, grammarly-alternative, macos
- [alphaparkinc/genpark-accessibility-tree-and-dom-action-selector-synthesizer-skill](https://github.com/alphaparkinc/genpark-accessibility-tree-and-dom-action-selector-synthesizer-skill) ★7 Python — Converts ARIA accessibility nodes and DOM elements into deterministic CSS/ARIA action selectors for browser agents  
  topics: accessibility-tree, action-synthesizer, agent-skills, aria-selector, browser-agent, deterministic-selectors, dom-selector, mcp
- [Alpha-Park/genpark-accessibility-tree-and-dom-action-selector-synthesizer-skill](https://github.com/Alpha-Park/genpark-accessibility-tree-and-dom-action-selector-synthesizer-skill) ★7 Python — Converts ARIA accessibility nodes and DOM elements into deterministic CSS/ARIA action selectors for browser agents  
  topics: accessibility-tree, action-synthesizer, agent-skills, aria-selector, browser-agent, deterministic-selectors, dom-selector, mcp
- [zakariaf/ReactNative-Skills](https://github.com/zakariaf/ReactNative-Skills) ★7 JavaScript — Deep, self-verifying React Native & Expo engineering skills for AI coding agents — 79 skills with checkers that prove the work: architecture, Expo Router, Zustand, TanStack Query, testing, i18n/RTL, a…  
  topics: agent-skills, ai-agents, best-practices, claude-code, codex, coding-agent, cursor, developer-tools
- [alphaparkinc/genpark-manus-autonomous-web-browser-dom-actuator-skill](https://github.com/alphaparkinc/genpark-manus-autonomous-web-browser-dom-actuator-skill) ★7 Python — Manus & Adept ACT-1-inspired Autonomous Web Browser DOM Actuator. Flattens DOM trees into accessibility trees (AXTree), prunes non-interactive noise, synthesizes robust CSS/XPath locators, and compile…  
  topics: agentic-commerce, gdpr-compliance, genpark, hume-ai, instacart, manus-ai, mcp, mcp-server
- [Alpha-Park/genpark-manus-autonomous-web-browser-dom-actuator-skill](https://github.com/Alpha-Park/genpark-manus-autonomous-web-browser-dom-actuator-skill) ★7 Python — Manus & Adept ACT-1-inspired Autonomous Web Browser DOM Actuator. Flattens DOM trees into accessibility trees (AXTree), prunes non-interactive noise, synthesizes robust CSS/XPath locators, and compile…  
  topics: agentic-commerce, gdpr-compliance, genpark, hume-ai, instacart, manus-ai, mcp, mcp-server
- [yuuki324/HideAccessibility](https://github.com/yuuki324/HideAccessibility) ★6 Kotlin — Make selected apps believe accessibility is off. libxposed API 102 port of Nitsuya/DoNotTryAccessibility. 让选定的应用以为本机没开启无障碍服务。  
  topics: 
- [medienbaecker/kirby-editoria11y](https://github.com/medienbaecker/kirby-editoria11y) ★6 PHP — Editoria11y accessibility checker for Kirby editors  
  topics: 
- [mtr1920/opstrellis](https://github.com/mtr1920/opstrellis) ★5 Rust — Voice dictation for macOS and Linux: hold a key, speak, and clean text appears in any app. Offline by default. Free for personal use.  
  topics: accessibility, developer-tools, dictation, linux, llm, macos, offline, productivity
- [rono-zeroseven/magic-pointer](https://github.com/rono-zeroseven/magic-pointer) ★5 C++ — Select anything on your Windows screen and ask Gemini, recognize text, translate, or search with Google Lens.  
  topics: accessibility, cpp, gemini, mouse, ocr, windhawk, windows
- [GhassenAZZOUZ/claude-qa-agent](https://github.com/GhassenAZZOUZ/claude-qa-agent) ★5 JavaScript — Eighteen QA workflows for Claude Code: Playwright-BDD UI, API, integration and multi-service tests, exploratory testing, bug filing, fix verification, PR test impact, flaky triage, release readiness, …  
  topics: accessibility, ai-agents, api-testing, azure-devops, bdd, bitbucket, claude-code, devops
- [WannaBeSolopreneur/YapYap](https://github.com/WannaBeSolopreneur/YapYap) ★5 Swift — Read any window aloud and dictate into any app. On-device text-to-speech and dictation for Mac.  
  topics: accessibility, dictation, macos, swift, text-to-speech
- [MorinelloA/ui-ux-audit-and-fix-prompt](https://github.com/MorinelloA/ui-ux-audit-and-fix-prompt) ★5  — A reusable prompt for Claude Code and OpenAI Codex that audits every screen of a web or React Native app across sizes, themes and text sizes, then fixes layout, touch targets and design-kit drift with…  
  topics: accessibility, ai-agents, claude-code, design-system, expo, openai-codex, playwright, prompt-engineering
- [triggeredcode/lucid](https://github.com/triggeredcode/lucid) ★5 TypeScript — Voice to structured notes and diagrams. Talk, and a local model builds the headings, lists, tables and diagrams while you think, then typesets a PDF. Hands-free or one-handed with an MCP toolbox for A…  
  topics: accessibility, assistive-technology, diagrams, dictation, electron, hands-free, latex, llm
- [linuxserver/docker-craft-apps](https://github.com/linuxserver/docker-craft-apps) ★5 Dockerfile — Web accessible PhotoCraft, VectorCraft, FilmCraft, LightCraft, PdfCraft, EffectCraft, FigCraft, and DesignCraft inside an Ubuntu Container  
  topics: 
- [RogueByteOfficial/ROGUEBYTE---Cybersecurity-Suite](https://github.com/RogueByteOfficial/ROGUEBYTE---Cybersecurity-Suite) ★5 Python — ROGUEBYTE — Defensive Cybersecurity & Network Operations Suite ROGUEBYTE has been engineered and built as a production-quality cybersecurity desktop workstation for Windows 10/11 and WSL2 (Ubuntu & Ka…  
  topics: 
- [heyedisonwong/iphone-esp32](https://github.com/heyedisonwong/iphone-esp32) ★4 C — iPhone automation with nothing but WiFi and a tiny board(ESP32-S3) — no pc, cable, jailbreak, App.  
  topics: accessibility, automation, ble, esp32, esp32-s3, firmware, hid, iphone
- [VitoorFranca/spokemark](https://github.com/VitoorFranca/spokemark) ★4 TypeScript — Real-time captions and transcripts for anything your Mac plays — calls, videos, podcasts. 100% on-device: CoreAudio Process Tap + whisper.cpp on Metal. No cloud, no audio leaves your Mac.  
  topics: accessibility, apple-silicon, captions, coreaudio, electron, live-captions, macos, meeting-notes
- [adiprmx/atlys](https://github.com/adiprmx/atlys) ★4 JavaScript — A curated collection of 47 skills for AI coding agents — design, writing, engineering.  
  topics: accessibility, agent-skills, ai-agents, ai-coding-assistant, android, claude-code, codex, copywriting
- [askdown/html](https://github.com/askdown/html) ★4 TypeScript — Render Askdown forms to accessible HTML, with a small vanilla JS runtime.  
  topics: 
- [UXLana/design-skills-pack](https://github.com/UXLana/design-skills-pack) ★4 HTML — Skills for Claude Code and Codex, for product designers: discovery, design systems, prototyping and QA, accessibility (WCAG 2.2 AA, 508, ADA Title II, EN 301 549), hand-off and case studies.  
  topics: 
- [dorkitude/embedding-local-cpu-vs-hosted](https://github.com/dorkitude/embedding-local-cpu-vs-hosted) ★4 HTML — Embedding retrieval study: local EmbeddingGemma vs hosted OpenAI/Qwen and accessible models; Go/Cobra + turbopuffer  
  topics: 
- [yales66/wispstage](https://github.com/yales66/wispstage) ★3 Swift — Lightweight end-to-end testing for SwiftUI Mac apps, built for coding agents.  
  topics: accessibility, claude-code, claude-code-plugin, coding-agents, e2e-testing, macos, swift, swiftui
- [Vichaya-Lab/g4speak](https://github.com/Vichaya-Lab/g4speak) ★3 Python — Voice-to-text for Windows — cloud transcription with on-device AI proofreading  
  topics: accessibility, dictation, offline-llm, pyside6, speech-to-text, thai, voice-to-text, whisper
- [monatis/okur](https://github.com/monatis/okur) ★3 Rust — A clean-room and cross-platform re-implementation of JAWS, built by AI agents with a sophisticated verification in the loop harness  
  topics: accessibility, accessibility-tools, clean-roo, jaws, screen-reader, tts-engines
- [thyhellcat/nrps](https://github.com/thyhellcat/nrps) ★3 Rust — Private relay server for NVDA Remote Access  
  topics: accessibility, nvda, relay, remote-access, rust, screen-reader
- [TheIdeaPlace/QuickDescribe](https://github.com/TheIdeaPlace/QuickDescribe) ★3 C# — Describes the screen, the active window, the focused item or a picture, with Windows' on-device AI. Built for JAWS, NVDA and Narrator.  
  topics: accessibility, copilot-plus-pc, image-description, jaws, narrator, nvda, ocr, screen-reader
- [Pranav435/stickersense](https://github.com/Pranav435/stickersense) ★3 C# — Describes chat stickers, GIFs and pictures out loud for screen reader users, on-device, in any app. Mac, iPhone and Windows.  
  topics: accessibility, blind, gif, ios, low-vision, macos, nvda, on-device-ai
- [Ar5en1c/youxpc](https://github.com/Ar5en1c/youxpc) ★3 Swift — Give your AI agent its own cursor: an MCP server that reads Mac windows as numbered text and presses controls through accessibility  
  topics: accessibility, ai-agents, computer-use, macos, mcp
- [oficiallyAkshay/ensemble](https://github.com/oficiallyAkshay/ensemble) ★3 Swift — Drive Claude desktop's Code sessions by where you look and what your hands do  
  topics: accessibility, claude, hand-tracking, macos, swift, webcam
- [Amulopapa67/TalkLens](https://github.com/Amulopapa67/TalkLens) ★3 Swift — Unofficial read-only translation overlay for KakaoTalk on macOS — on-device Apple Translation, open source  
  topics: accessibility, immersive-translation, kakaotalk, korean, macos, menubar-app, swift, translation
- [Tetrismonster/Musician-Containment-Facility](https://github.com/Tetrismonster/Musician-Containment-Facility) ★3 Python — Accessible local music generation for screen reader users  
  topics: 
- [YigitEfe-DEV/website-bug-hunter](https://github.com/YigitEfe-DEV/website-bug-hunter) ★3 TypeScript — Open-source website bug & quality scanner — broken links, broken images, JS console errors, redirect anomalies, missing metadata, accessibility, mobile responsiveness.  
  topics: 
- [nickfrostech/esvigy](https://github.com/nickfrostech/esvigy) ★3 TypeScript — The "Lucide for illustrations" — 100% vector, tree-shakable UI illustrations as simple as icons. Features dual-layer two-tone theming, zero-JS GPU micro-animations, automatic dark mode adaptation, and…  
  topics: design-system, flowbite, icons, illustrations, illustrator-free, lucide, micro-animations, open-source

### 活発な既存リポジトリ (stars≥200, 期間内に push)

- [chakra-ui/chakra-ui](https://github.com/chakra-ui/chakra-ui) ★40690 — Chakra UI is a component system for building SaaS products with speed ⚡️
- [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) ★29742 — PDF Parser for AI-ready data. Automate PDF accessibility. Open-source.
- [ariakit/ariakit](https://github.com/ariakit/ariakit) ★8627 — Toolkit with accessible components, styles, and examples for your next web app
- [grommet/grommet](https://github.com/grommet/grommet) ★8352 — a react-based framework that provides accessibility, modularity, responsiveness, and theming in a tidy package
- [dequelabs/axe-core](https://github.com/dequelabs/axe-core) ★7667 — Accessibility engine for automated Web UI testing
- [unovue/reka-ui](https://github.com/unovue/reka-ui) ★6884 — An open-source UI component library for building high-quality, accessible design systems and web apps for Vue. Previously Radix Vue
- [skeletonlabs/skeleton](https://github.com/skeletonlabs/skeleton) ★6079 — Skeleton is an adaptive design system powered by Tailwind CSS.
- [chakra-ui/zag](https://github.com/chakra-ui/zag) ★5234 — Build your design system in React, Solid, Vue, Svelte or Vanilla. Powered by finite state machines
- [nvaccess/nvda](https://github.com/nvaccess/nvda) ★2664 — NVDA, the free and open source Screen Reader for Microsoft Windows
- [iFurySt/open-computer-use](https://github.com/iFurySt/open-computer-use) ★2499 — 👾 Open Computer Use – Open-Source Alternative to Codex Computer Use
- [Fate-Grand-Automata/FGA](https://github.com/Fate-Grand-Automata/FGA) ★2406 — Auto-battle app for F/GO Android
- [mlaursen/react-md](https://github.com/mlaursen/react-md) ★2325 — React material design - An accessible React component library built from the Material Design guidelines in Sass
- [Core-Mate/OpenGUI](https://github.com/Core-Mate/OpenGUI) ★1819 — OpenGUI is an Android GUI agent framework for phone-use AI that can see, plan, and operate real mobile apps through the GUI.
- [incluud/accessible-astro-starter](https://github.com/incluud/accessible-astro-starter) ★1189 — An Accessible, WCAG compliant Starter Theme for Astro 6+ including several accessibility features such as, better focus-outline, landmarks, semantics, interactive components and skip-link navigation. …
- [vue-final/vue-final-modal](https://github.com/vue-final/vue-final-modal) ★1013 — 🍕Vue Final Modal is a tiny, renderless, mobile-friendly, feature-rich modal component for Vue.js.
- [ooade/NextSimpleStarter](https://github.com/ooade/NextSimpleStarter) ★949 — :whale: Simple and Accessible PWA boilerplate with Nextjs 15 and MUI
- [lukasbach/headless-tree](https://github.com/lukasbach/headless-tree) ★908 — The definitive tree component for the Web
- [y3owk1n/neru](https://github.com/y3owk1n/neru) ★831 — Hints, grids and vim keys for your whole desktop. Built for macOS, linux and windows, natively.
- [franzenzenhofer/big-arrow-on-the-screen](https://github.com/franzenzenhofer/big-arrow-on-the-screen) ★781 — Let your AI agents paint big arrows, boxes and text on your Mac screen. One CLI, click-through, gone by itself. Skill for Claude Code and Codex. MIT.
- [cashapp/AccessibilitySnapshot](https://github.com/cashapp/AccessibilitySnapshot) ★748 — Easy regression testing for iOS accessibility
- [vuetifyjs/0](https://github.com/vuetifyjs/0) ★740 — 0️⃣ Composable UI engine for Vue. Build complex interfaces with reusable state, logic, and primitives—without being locked into components or styles.
- [guidepup/guidepup](https://github.com/guidepup/guidepup) ★577 — Screen reader automation library for testing.
- [fecarrico/A11Y.md](https://github.com/fecarrico/A11Y.md) ★470 — A context system for building accessible software by default — for developers and AI, with enforceable rules aligned to WCAG.
- [vmware-clarity/ng-clarity](https://github.com/vmware-clarity/ng-clarity) ★433 — Clarity Angular is a scalable, accessible, customizable, open-source design system built for Angular.
- [toyota-connected/ivi-homescreen](https://github.com/toyota-connected/ivi-homescreen) ★401 — Flutter Linux C++ embedder for desktop and embedded/automotive displays — Wayland, DRM/KMS, EGL, Vulkan (incl. zero-copy dma-buf), and software backends
- [janosh/svelte-widgets](https://github.com/janosh/svelte-widgets) ★385 — Accessible Svelte components, attachments, and Markdown tools for interactive apps and documentation.
- [cvs-health/ios-swiftui-accessibility-techniques](https://github.com/cvs-health/ios-swiftui-accessibility-techniques) ★385 — Demonstrates iOS SwiftUI Accessibility programming techniques using live good and bad examples that can be tested with VoiceOver and other AT. Includes documentation for developers explaining how to c…
- [openclaw/AXorcist](https://github.com/openclaw/AXorcist) ★327 — AXorcist • Swift wrapper for macOS Accessibility—chainable, fuzzy-matched queries that read, click, and inspect any UI. The power of Swift compels your UI to obey!
- [public-ui/kolibri](https://github.com/public-ui/kolibri) ★287 — The accessible HTML-Standard
- [niki914/zafiro](https://github.com/niki914/zafiro) ★270 — Open-source BYOK AI agent for Android. Full phone control, native Shell & Python 3, with Skills and MCP support. Built with Material 3 Expressive. Works via Shizuku (root optional). Bring any provider…
- [nuxt/a11y](https://github.com/nuxt/a11y) ★233 — Nuxt module to provide accessibility hinting and utilities.
- [felix-berlin/astro-breadcrumbs](https://github.com/felix-berlin/astro-breadcrumbs) ★226 — Well configurable breadcrumb component for Astro.js. Create breadcrumbs completely dynamically or specify exactly how they should look.
- [Samyssmile/notectl](https://github.com/Samyssmile/notectl) ★206 — Modern Accessible WYSIWYG rich text editor built as a framework-agnostic Web Component that works everywhere.
- [nuxt-modules/html-validator](https://github.com/nuxt-modules/html-validator) ★203 — HTML validation for Nuxt

## 6. Awesome 系リストへの追加

(なし)

## 取得失敗

(なし)
