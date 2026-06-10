# The Unofficial Guide — Project 1

> **How to use this template:**
> Complete each section *after* you've built and tested the corresponding part of your system.
> Do not write placeholder text — if a section isn't done yet, leave it blank and come back.
> Every section below is required for submission. One-liners will not receive full credit.

---

## Domain

<!-- What topic or category of knowledge does your system cover?
     Why is this knowledge valuable, and why is it hard to find through official channels?
     Example: "Student reviews of CS professors at [university] — useful because official
     course descriptions don't reflect teaching style, exam difficulty, or workload." -->
     The domain chosen is off-campus housing options and reviews (UCF). This knowledge is valuable to new (transfer) students or students transferring out of campus housing, to allow them to make an informed decision and to have the best experience possible. Whilst UCF offers a list of off-campus options, it does not provide further information or reviews. 

---

## Document Sources

<!-- List every source you collected documents from.
     Be specific: include URLs, subreddit names, forum thread titles, or file names.
     Aim for variety — sources that together cover different subtopics or perspectives. -->

| # | Source | Type | URL or file path |
|---|--------|------|-----------------|
| 1 | UCF Website | List of Off-Campus shuttle routes and corresponding off-campus housing stops|https://parking.ucf.edu/transportation/off-campus/  | 
| 2 | Unofficial UCF Reddit | Post about the experience of looking for off-campus housing and not finding a good option, comments share experiences and recommendations | https://www.reddit.com/r/ucf/comments/1i1bv63/why_does_ucf_not_have_any_good_apartment_options/ |
| 3 | Unofficial UCF Reddit | Post about worst housing experiences, commments explore different points of view and experiences at particular places| https://www.reddit.com/r/ucf/comments/1agryxz/whats_the_worst_housing_in_the_ucf_area/ |
| 4 | Unofficial UCF Reddit | Post asking for off-campus housing horror stories, comments mention experiences (some mentioning places/complexes names) | https://www.reddit.com/r/ucf/comments/1tgsx72/please_tell_me_your_offcampus_housing_horror/ |
| 5 | Unofficial UCF Reddit | Post asking about best off-campus complexes, comments talka about pricing and experiences | https://www.reddit.com/r/ucf/comments/1r2n0ud/best_off_campus_complexes/ |
| 6 | Unofficial UCF Reddit | Post from a year ago asking about best housing options, comments share both good and bad experiences in multiple places | https://www.reddit.com/r/ucf/comments/1e7dmvz/best_offcampus_housing/ |
| 7 | Unofficial UCF Reddit | Post asking about on-campus vs off-campus for freshman year | https://www.reddit.com/r/ucf/comments/1gu04yt/on_or_off_campus_housing/ |
| 8 | Unofficial UCF Reddit | Post asking about experiences between 3 off-campus options (Mercury 3100, Lofts, Hub), comments expand on them but also suggest others | https://www.reddit.com/r/ucf/comments/1kohehb/which_off_campus_housing_should_i_move_in/ |
| 9 | Unofficial UCF Reddit | Recent post about affordable off campus options (less than 1k)| https://www.reddit.com/r/ucf/comments/1qmomqs/off_campus_housing/ |
| 10 | Unofficial UCF Reddit | Post asking about how off-campus shuttles work, comments explain and share experiences | https://www.reddit.com/r/ucf/comments/p63pou/how_does_offcampus_shuttles_work/ |


---

## Chunking Strategy

<!-- Describe your chunking approach with enough specificity that someone else could reproduce it.
     Include:
     - Chunk size (characters or tokens) and why that size fits your documents
     - Overlap size and why (or why not) you used overlap
     - Any preprocessing you did before chunking (e.g., stripping HTML, removing headers)
     - What your final chunk count was across all documents -->

**Chunk size:**

**Overlap:**

**Why these choices fit your documents:**

**Final chunk count:**

---

## Embedding Model

<!-- Name the embedding model you used and explain your choice.
     Then answer: if you were deploying this system for real users and cost wasn't a constraint,
     what tradeoffs would you weigh in choosing a different model?
     Consider: context length limits, multilingual support, accuracy on domain-specific text,
     latency, and local vs. API-hosted. -->

**Model used:**

**Production tradeoff reflection:**

---

## Grounded Generation

<!-- Explain how your system enforces grounding — how does it prevent the LLM from answering
     beyond the retrieved documents?
     Describe both your system prompt (what instruction you gave the model) and any structural
     choices (e.g., how you formatted the context, whether you filtered low-relevance chunks).
     Do not just say "I told it to use the documents" — show the actual instruction or explain
     the mechanism. -->

**System prompt grounding instruction:**

**How source attribution is surfaced in the response:**

---

## Evaluation Report

<!-- Run your 5 test questions from planning.md through your system and record the results.
     Be honest — a partially accurate or inaccurate result that you explain well is more
     valuable than a suspiciously perfect result. -->

| # | Question | Expected answer | System response (summarized) | Retrieval quality | Response accuracy |
|---|----------|-----------------|------------------------------|-------------------|-------------------|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |

**Retrieval quality:** Relevant / Partially relevant / Off-target  
**Response accuracy:** Accurate / Partially accurate / Inaccurate

---

## Failure Case Analysis

<!-- Identify at least one question where retrieval or generation did not work as expected.
     Write a specific explanation of *why* it failed, tied to a part of the pipeline.

     "The answer was wrong" is not an explanation.

     "The relevant information was split across a chunk boundary, so retrieval returned
     only half the context — the model didn't have enough to answer correctly" is an explanation.

     "The embedding model treated the professor's nickname as out-of-vocabulary and returned
     results from an unrelated review" is an explanation. -->

**Question that failed:**

**What the system returned:**

**Root cause (tied to a specific pipeline stage):**

**What you would change to fix it:**

---

## Spec Reflection

<!-- Reflect on how planning.md shaped your implementation.
     Answer both questions with at least 2–3 sentences each. -->

**One way the spec helped you during implementation:**

**One way your implementation diverged from the spec, and why:**

---

## AI Usage

<!-- Describe at least 2 specific instances where you used an AI tool during this project.
     For each: what did you give the AI as input, what did it produce, and what did you
     change, override, or direct differently?

     "I used Claude to help me code" is not sufficient.
     "I gave Claude my Chunking Strategy section from planning.md and asked it to implement
     chunk_text(). It returned a function using a fixed character split. I overrode the
     chunk size from 500 to 200 because my documents are short reviews, not long guides." -->

**Instance 1**

- *What I gave the AI:*
- *What it produced:*
- *What I changed or overrode:*

**Instance 2**

- *What I gave the AI:*
- *What it produced:*
- *What I changed or overrode:*
