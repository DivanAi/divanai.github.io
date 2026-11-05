# DivanAI — many AI minds, one table

**Site:** https://divanai.github.io/  ·  **Source:** https://github.com/divanai/divanai.github.io

**English** · [Türkçe](README.md) — the interface is bilingual: flip it with the two flags in the top bar.

> **Divan** was the Ottoman council where state affairs were debated; the **AI** suffix carries it to
> artificial intelligence. Pronounced *di-va-na-i*. Correct spelling: **divanai** (one word, lower case).

You write a topic; the AI minds at the table speak in turn, challenge each other, and at the end the
chair sums it up. No tab-by-tab copy-paste.

**One file.** Double-click `index.html` and it opens. No install, no account, no server.
**Keyless demo.** Try the whole flow without signing up anywhere (demo text is never passed off as a
live answer).

| **Council** | **Panel** | **Mirror** | **Agents** | **OneOnOne** |
|---|---|---|---|---|
| ![Council](ekranlar/1-konsey.jpg) | ![Panel](ekranlar/27-panel.jpg) | ![Mirror](ekranlar/3-ayna.jpg) | ![Agents](ekranlar/11-ajan-kurulum.jpg) | ![OneOnOne](ekranlar/26-teketek.jpg) |
| Models from 3–5 different companies, roles, a chair summary | Seats answer **at once**, blind to each other; **the comparison is yours** | One model in two seats: defender + objector, judge verdict | A task per seat, chained hand-off, one delivery | A single AI, direct answer; the keyless option is **slow** |

If you just want a plain chat, pick **OneOnOne**: one AI at the table answers directly. A **keyless
option ships ready** (gpt-oss 20B, through Pollinations) — real answers with no signup; it is slow
(5–8 seconds in my measurement), so a proper test is better with a free key.

---

## Quick start (30 seconds)

1. Download the `divanai` folder and double-click **`index.html`**. (No Python, no install, no internet needed.)
2. Pick the table type at the top: **Council · Panel · Mirror · Agents · OneOnOne**.

**Start with no setup at all.** The app opens in **Live** mode and sets up **three keyless seats**:
**Pollinations** (gpt-oss 20B), **LLM7.io** (Mistral Nemo), **OVH AI Endpoints** (Llama 3.3 70B) — three
separate services, **no signup, no key, no card**. The first round is slow: when I measured it, the three
answers arrived in **~21 seconds** in parallel (LLM7 takes one request at a time, OVH two a minute).
**OneOnOne** also works keyless (Pollinations); there the answers arrive one after another.
3. Type the topic into the box and press `Enter`. *(Example: "Is opening a small coffee shop in Bursa sensible?")
4. In demo mode the answers are canned text; you see the flow and **no requests are spent**.

**Faster is optional (3 steps):** ① create an account with a free provider — the most generous free tier
is **Google AI Studio** (no credit card, and the daily allowance is counted **per model**); ② copy the
key, ③ Settings → **Free · your own key** → **Google AI Studio** → paste the key → **⇅ Test connection** →
**Save and apply**. Clicking a connection card applies that service to **every seat**; the app tells you so
with a notice. Paid services (**Vercel, Requesty, NanoGPT, AIMLAPI**…) are not in the main list — they sit
folded under **Other services**, so leave them closed unless you need them. Every card carries a
**no card / card required** tag.
The key is kept **in this browser only** (`localStorage`); it never goes to a server, a file or a store.
To try something free, put an id ending in `:free` — e.g. `google/gemma-4-31b-it:free`.

![Settings — three keyless seats](ekranlar/30-ayarlar-sade.jpg)

*Settings opens like this: mode at the top, then the **three keyless services** (Pollinations · LLM7.io ·
OVH), then free services that need a key; paid ones stay folded under **Other services**.*

**On a phone:** the same file works; the layout holds down to 360 px.

---

## Using it

### 1 · Set the table

| What | Where | Note |
|---|---|---|
| **Table type** | The four buttons at the top | Switching clears the current conversation (it warns first) |
| **Topic** | The input box at the bottom | `Enter` starts, `Shift+Enter` new line |
| **Attach a file** | The **paperclip** left of the text box | Image · PDF · Word (.docx) · Excel (.xlsx) · PowerPoint (.pptx) · text/code. You can also paste with **Ctrl+V** or drag and drop. In **every mode** the file goes to the seats with that question |
| **Agenda** | The chips under the topic | **Generate ideas · Debate & critique · Decide** — Council only; Mirror's agenda is fixed |
| **Language** | The two flags in the top bar (Turkish · English) | Translates the whole interface TR ⇄ EN; the choice is remembered. Answers and your topic are never translated |
| **Model** | The picker next to the list in Mirror and OneOnOne | In OneOnOne: **Pollinations · keyless** or **your own connection** |
| **History** | The clock icon in the top bar | Last 10 conversations in this browser + **favorites** · open, continue, delete |
| **Don't show again** | Top right of the key card | Hides the “3 steps to live models” card for good (turns off the key prompt on the main screen) |

**While the conversation runs:**
- You can drop a **note** at the bottom — the next speakers see it.
- **Stop** cuts the table instantly; answers already written are kept.

### 1b · History and moving between devices

No account, no login. So that conversations are not lost, there are three things:

| What | Where | What it does |
|---|---|---|
| **Last session** | Automatic | Reload the page or reopen the tab and the conversation is still there |
| **History list** | Top bar → **clock icon** | The last **10 conversations** in this browser: date, mode, message count. Click one → continue where you stopped. `×` deletes one by one, the button at the bottom clears all |
| **Favorites** | The **star** (☆) on a row | Mark an important conversation: it stays **at the top** in its own section and the limit of 10 **does not delete it** (up to 30 favorites) |
| **Session file** | Same panel → **Save session to file / Open from file** | A `.json` file to move to another device. Send it to yourself over WhatsApp/Drive/email and open it there |

The history list lives **only in that browser's store**; it never goes to a server and needs no account.
If you clear browser data the list goes too — so **save** important conversations to a file or use
**Export**. Images themselves are not stored (to save space); an old conversation opened from the list
shows the image box as “lost”.

### 2 · When a round ends

| Button | What it does |
|---|---|
| **+ One more round** | Deepens the same topic; the chair's closing is renewed |
| **Summarize** | The chair's decision in one card: Result · pros/cons · first step |
| **Export** | **Word (.docx)** · **Text (.txt)** · **Markdown (.md)** — the file is built in the browser |
| **Copy** | The whole table to the clipboard as markdown |
| **New table** | Clears the conversation and the pause record |

The table is **saved automatically**: reload and the last session comes back. Conversation history is
not part of the settings backup; take it with **Export**.

### 3 · Settings (what you actually need)

**Models at the table**
- Turn each seat on or off (at least one must stay on). DivanAI knows five providers:
  ChatGPT, Gemini, Claude, Grok, DeepSeek — **all five** can be on at once.
- **Paste the key and models appear by themselves**: the chosen service's own model list is fetched and
  models from that service land on the five seats. No need to type model ids by hand. A model you picked
  yourself, if the service has it, is **kept**, not overwritten.
- **Chair**: the seat that writes the summary and the closing.
- The **Free models** button lists the `:free` models your key can see; pick **which seat** first, then
  press **use** on the row. No seat changes until you choose. **+ New seat** adds a provider that is not
  at the table yet.

**Conversation settings**

| Setting | What it does | Default |
|---|---|---|
| **Tone** | Natural chat (short sentences, no filler) · Report layout (Result/Pros/Cons/First step) · Brief points | **Natural chat** |
| **Answer limit** | Max words per speaker (30–500) | 130 |
| **Context** | Table memory (fewest tokens) · Compressed · Full history | **Table memory** |
| **Max rounds** | Round cap (2–20); when full the table stops and summarizes | 6 |
| **Stop when saturated** | Stops by itself if the last two rounds bring nothing new | On |
| **Web search** | Works on OpenRouter only and **spends credits**; leaving it off is free | Off |

**Connection**
To stay free, start with **Google AI Studio**: no credit card, the Flash and Flash-Lite models are free,
and the daily allowance is counted **per model** — so four seats on four different Gemini models use four
separate allowances. (The exact daily numbers live in AI Studio → *Rate limits*; Google can change them
per country.) It reads images, so you can attach a photo. **Z.ai (GLM)** is card-free too: GLM-4.7-Flash and GLM-4.5-Flash are listed as *free* with no
published request quota (a per-minute limit may apply). Two **keyless** options also exist: **LLM7.io**
(1 request at a time) and **OVH AI Endpoints** (2 requests a minute) — single-seat only, but no signup.
**OpenRouter** gives many models behind one key
(free `:free` models, **50 requests a day**); **Groq** is the fast one (**1,000 a day**, but 8k tokens a
minute). If you want a single provider you can connect directly with its own key — **Groq, DeepSeek,
Mistral, xAI, OpenAI**. **Cerebras** no longer offers a permanent free tier (a 30-day $5 trial credit,
with a verified payment method). Groq's free models changed as well: **llama-3.1/3.3 were removed on
16 August 2026**, so the preset now uses `openai/gpt-oss-120b`, `openai/gpt-oss-20b` and `qwen/qwen3.8-27b`. Your own OpenAI-compatible address (LiteLLM, Cloudflare AI Gateway) goes on the **Custom
address** card. The key never reaches any server: it stays in your browser.

![Connection test and diagnostics](ekranlar/10-teshis.jpg)

**⇅ Test connection** sends a one-word request to every open seat and reports line by line:
`✕ Claude · 401 invalid api key` (wrong key), `✕ Grok · 404 model not found` (wrong model id),
`429` (quota), CORS (browser blocked). On a connection problem, **run this first.**

> If you get **403 "Key limit exceeded"**, the key is valid but its **spend limit** is zero.
> Go to `openrouter.ai/settings/keys` → the key → raise **Limit** (adding credit alone is not enough).

**Per-seat connection.** Each seat can use its own provider; the daily free allowance stacks. Example:
ChatGPT → **Google AI Studio** (Gemini 3.8 Flash), Gemini → **Google AI Studio** (Gemini 3.5 Flash-Lite),
Claude → **Google AI Studio** (Gemini 3.6 Flash), Grok → **Groq** (1,000/day). All four are card-free;
three of them are Gemini models, so they draw on three separate model allowances. A seat with its own connection that hits 429 rests **alone**; on a shared connection
all seats rest together (see *Not wasting tokens* below). Settings → *Models at the table* → the list
under the row. A seat with its own connection shows a badge such as `⛁ Groq` on the table screen.

![Per-seat connection](ekranlar/9-sandalye-baglanti.jpg)

**Daily quota.** The bottom bar shows `7 / 50` and `resets in 23h 24m` (green: plenty, yellow: low,
red: out). Click the label → the quota box opens. OpenRouter free allowance is **50 a day**, reset at
**03:00**; Groq **1,000/day**; Gemini depends on the model, **10:00**. The counter spends no requests.
For services whose reset time is unknown the app does **not invent a clock** — it says “at the provider's
own daily reset”.

**When the quota runs out.** Two cases:

- **Every seat on its own service** (the default setup: Pollinations · LLM7 · OVH): only the seat whose quota
  ran out stops, with a one-line notice (`Mistral Nemo is done for today…`). **The table carries on** —
  the other seats keep talking on their own services.
- **Seats sharing one key** (a single Google/OpenRouter key): they all draw from the same pool, so the
  table stays where it is and a green button appears:
**▶ Continue where you left off · 3 speakers**. Press it once the allowance resets; **only the missing**
seats run, nothing is regenerated from scratch. Close the site and the state is remembered. With quota
at 0 the Summarize button sends no request at all and builds a **local summary** from the sentences on
the table (card title: “Local summary · no model called”).

![Quota out: local summary + continue](ekranlar/18-kota-devam.jpg)

**Backup.** Settings live **in this browser**. Move them with *Download backup (.json)* / *Load from
backup*. Keys are **not written** to the file by default; tick the box and it carries them as plain
text (a red warning appears). If the backup has no keys, the keys in this browser are kept; a broken
file changes nothing.

![Backup](ekranlar/15-yedekleme.jpg)

**Table memory (default).** Every seat does not re-read the whole history before speaking. The app
shrinks old rounds into one-line notes; the model receives only **your first question + that note + the
last two messages**. The note is **invisible** on screen — it only cuts token spending. On the same
table spending drops roughly six-fold: 10–15 tables a day instead of 2–3.

**Three rules against wasting tokens.** All under Settings → *Token saving*; switch them off if you like.

- **Passing (on, Council).** From round 2 on, a seat with nothing new to say writes no answer and just
  says `PASS`. There is no passing in round 1 or for the closing speaker (the chair); Mirror and Agents
  have none at all. One line appears on the table: *"Gemini saw no new point · passed, no answer written."*
- **Seat timeout (120 s).** If a seat cannot finish in time **only that seat** is cut, the table does not
  hang. Text longer than 30 characters is **kept** and placed on the table marked “cut short”.
- **Provider cooldown (1 min).** A **connection** that returns 429 or “out of credits” is not tried at
  all for this period; the seat shows `resting · 16:19`. If all are resting the table pauses and resumes
  with **▶ Continue where you left off** when the time is up. **End cooldown** reopens without waiting.

On a shared key (OpenRouter, say) a 429 is **account-wide**: if one seat hits the wall, every seat on the
same connection rests. Give each seat its own connection and each spends its own allowance.

**Where does it apply?** Timeout and cooldown work in **all three table types** (in Agents the chain does
not hang either; the step of a resting connection is skipped). Passing exists only in **Council**. The
daily quota does not create a cooldown — waiting 5 minutes does not fix it; that is what the pause and
**Continue where you left off** are for. The continue button is an explicit intervention: it also lifts
any cooldown wait.

![Token saving settings](ekranlar/23-token-tasarrufu.jpg)

![All seats resting: table paused](ekranlar/24-dinlenme.jpg)

---

## Attaching files and images

![Attaching files: PDF, image and Excel in the tray](ekranlar/28-dosya-ekleme.jpg)

Use the **paperclip** left of the text box (or **Ctrl+V** / drag and drop) to attach a file to your question.
A small **tray** appears above the box with the file name, size, page count and a ✕ button. Press `Enter` and
the file goes to **every seat at the table** with that question; they all read the same document.

| File | What happens |
|---|---|
| **Image** (png · jpg · webp …) | Long edge is reduced to 896 px and sent **as an image**. Only vision-capable models can comment on it (most of the GPT, Gemini, Claude and Grok families via OpenRouter). **The keyless option cannot read images** (measured: it returns 400); the app then skips the image, shows a one-line warning and continues with the document text. |
| **PDF** | The **selectable text** is extracted (in your browser, no add-ons). If a scanned PDF has no text, the app says so: upload a screenshot of the page instead. |
| **Word (.docx)** | Paragraphs and tables become text. |
| **Excel (.xlsx)** | Sheet by sheet, cells become **tab-separated** text. |
| **PowerPoint (.pptx)** | Text is pulled slide by slide. |
| **Text / code** (.txt · .md · .csv · .json · .html · .js · .py …) | Added as is; HTML tags are stripped. |

If a connection has no vision (or the model rejects images) the app notices: it strips the images, retries
**once**, shows a one-line warning and never sends images to that connection again. Document text always goes
through.

Limits: one file **25 MB**, **6 files** per message, **24k characters** per document (the beginning is kept
and the app tells you). Files are read **in your browser** and never uploaded anywhere — they only travel to
the model provider you picked, inside the request body. An image is not resent every round: it rides along
in the message it arrived in and in the **next** one, then it is only referenced as text.

## Panel

![Panel: four seats at once, blind to each other](ekranlar/27-panel.jpg)

Seats answer **at the same time** and **do not see each other**: each seat only sees your questions and
**its own** earlier answers. No chair, no summary, no judge — the views are written one under the other and
**the comparison is yours**. Pick this when you want to see what four models say about the same question,
side by side and without influence. Each message costs one request per seat (4 seats = 4 requests) and the
four answers arrive together; you do not wait in turn.

## Council

![Council conversation](ekranlar/2-konsey-konusma.jpg)

3–5 separate models at one table; each has a role and the chair has the last word.

| Seat | Role | What it does |
|---|---|---|
| ChatGPT | **Moderator** | Opens the table, runs the debate |
| Gemini | **Analyst** | Splits the topic into layers, sets criteria and assumptions |
| Claude | **Critic** | Flags weak points, risks, hidden costs |
| Grok | **Engineer** | Feasibility, steps, timing |
| DeepSeek | **Researcher** | Data, examples, comparisons (off by default) |
| One of them | **Chair** | Has the last word, writes the summary |

Roles are not sticky: turn models on and off, change the chair, rewrite the roles. The heading follows
the setting too — with 5 seats open it reads “Five AI minds, one table”.

![Five seats](ekranlar/19-bes-sandalye.jpg)

**Three rules for every speaker** (baked into the system prompt): **short** (no decoration, no intro
lines), **objective** (no invented numbers or prices; with no data it says “no evidence”), **no
repetition** (no restating what was already said, no “X said that”). With nothing new it says so plainly.

---

## OneOnOne

![OneOnOne · keyless](ekranlar/26-teketek.jpg)

A single AI at the table; no debate, no turns, no chair. It answers what you write and keeps the chat's
memory as you continue. Two options:

| Option | What it needs | When |
|---|---|---|
| **Pollinations · keyless** | Nothing — no signup, no key | First try, single question, free use |
| **My own connection** | A provider + key in Settings → Connection | You already have a key, you want no limits |

**The keyless option has a limit:** Pollinations publishes no quota; under load it throttles requests
(in my measurement answers arrived in 5–8 seconds). If the server returns a 402 the app says how many
seconds to wait and retries once by itself — you never see an empty error screen. The server runs best-effort and may slow down now and then. The model's **inner reasoning**
is not printed, only the answer. The chat is not saved anywhere; since no key is used there is nothing
to lose.

---

## Mirror

One model takes two seats: **A defends, B objects**. In the first round A opens; in the second round
**B opens and A objects** — so neither side is stuck defending. At the end the same model writes a
verdict as a **neutral judge**: which side is right where, the strongest 2+2 arguments of defence and
objection, the point that cannot be decided and the data that would settle it, and the first step.

- **+ One more round**: a new round is played, the verdict is renewed (the old verdict card is removed).
- Mirror has **no agenda picker** — it is always *debate & critique*.
- Cost: **2 rounds + verdict = 5 requests** (single model).

![Mirror · judge verdict](ekranlar/4-ayna-hakem.jpg)

---

## Agents

Council and Mirror **debate** a question; Agents **do** a project.

1. Write the **project** (one sentence): *"Draw up a 6-week launch plan for a small handmade soap brand."*
2. Give each seat a **Task** and an **Expected output**. The second is the acceptance criterion. An agent
   left empty is skipped.
3. Pick the **flow** (table below).
4. Send. Agents work in turn and every step shows on screen (**1 ✓ 2 ● 3 · 4 ·**).
5. At the end a **TEAM DELIVERY** card appears: summary, who did what, the real output, what is still
   open, first step.
6. Not enough? **+ One more pass**: the agents now try to close what the previous pass left open.

| Flow | What it does | Requests |
|---|---|---|
| **Sequential** (default) | 1 → 2 → 3 → 4; each agent gets the previous one's hand-off package | 4 agents + merge = **5** |
| **Supervisor** | The chair splits the work first, agents follow the plan, the chair merges | **6** |
| **Relay** | Each agent picks the next one; stops on "DONE" | cap **8** |

**How many agents (2…5).** The **Agent count** picker at the top right of the setup: `2` · `3` ·
`4 (all)`. It only **narrows** — the first N open seats run, the roster is not deleted; the **≈ N
requests** estimate above drops. The **＋ Add DeepSeek** button opens the fifth seat in one click.

![Agent count](ekranlar/17-ajan-sayi.jpg)

**Pause at every step.** Ticked, you press **Continue** after each agent, so you can cut a chain that is
going wrong. **Passes: 1 / 2 / 3** runs the same roster several times.

**Ready roster.** The **Roster** button at the top right of each seat card: **12 Turkish templates** +
**268 English expert entries**. Search works in both languages (`finans` finds *Financial analyst* and
*finance*). A pick is written **only to that seat**: role + task + expected output. On a filled seat it
asks first.

![Ready roster](ekranlar/16-kadro.jpg)

**Hand-off package.** Each agent appends a structured package to its answer (GOAL · SETTLED · OPEN ·
EVIDENCE · CONSTRAINT · LIMIT · NEXT). The next agent sees **only this package**, not the whole
conversation: cost does not grow quadratically along the chain and constraints do not get lost.

**Reset.** **✦ Clear** in the setup clears tasks, the project sentence and the conversation.

**In demo mode** what runs is the **skeleton** of the agent flow: tasks turn into packages, the merge
works, 0 requests spent. Text is labelled “(Demo)” and never passed off as a live answer.

---

## Images (Agents)

In the setup, tick **"Draw an image from this agent's text"** under a seat card; that agent draws an
image after finishing its text. In the ready projects it is pre-ticked for **Magazine issue** (cover),
**Restaurant opening** (storefront) and **Product launch** (campaign image).

> **The agent does not draw the image itself.** ChatGPT/Gemini/Claude/Grok produce text; the image is
> drawn by the selected **image engine**. The agent only writes the prompt (the `IMAGE PROMPT:` line in
> its answer; if absent, *GOAL* in the hand-off package; if that is absent too, the first 260 characters).

| Engine | Key | Cost | Limit | Note |
|---|---|---|---|---|
| **Free** (default) | Not needed | **0** | **1 image per 45 s** per IP | Small `pollinations.ai` watermark bottom right; weak at text/letters, long edge 1024 px |
| **OpenRouter** | Your own key | ~**$0.001–0.003** per image | The provider's limit | No watermark, high quality; **asks once per session** |

**Ratio.** Six buttons on the IMAGE row: `1:1` square · `4:3` card · `3:2` photo · `16:9` wide · `9:16`
vertical · `21:9` cinema. The choice is remembered and shows as a label on the card. The size written on
the card is the size actually requested (the free engine keeps the long edge at 1024 and DivanAI
downloads accordingly).

**Camera tags.** `Morning light · Portrait · Wide angle · Product shot · Cinematic · Flat drawing` —
they **append text to the image prompt**; no credits, no model change. Press again to turn off; a part
already present in the prompt is not repeated.

![Image ratio and camera tag](ekranlar/22-gorsel-oran.jpg)

**Behaviour**
- An image is a **separate request**; it does not count as agent chat. It reads “≈ 5 requests · 1 image (free)”.
- In live mode, before starting you are **asked** how many images will be drawn and which engine is used;
  decline and the text part still completes.
- **No images in demo mode** (no network). To try one by one, use the **🖼 Generate image** button at the
  top of an answer.
- At the rate limit the card counts down “Image queued · N s”. If the server answers busy (503), DivanAI
  retries **once** after 6 seconds.
- **Images are not stored** (so they do not fill browser quota). Reload the page and the picture is gone;
  **Regenerate** brings it back. Export writes the **prompt**, not the image.

![Image generation](ekranlar/14-gorsel-uretim.jpg)

---

## Language

**The interface is bilingual: Turkish and English.** Press one of the two flags in the top bar and all
text switches — buttons, help, settings, warnings, confirmation boxes, export headings. The choice is
stored in the browser and survives a reload. On first open, if the browser language is not Turkish, the
interface starts in English.

Answers come **in the language you write**: Turkish if you write Turkish, English if you write English.
The app detects the topic's language and adds it to every model's instruction.

**What is not translated:** your topic, the chat bubbles and the model answers. They belong to you and
stay exactly as written whatever the interface language. **Demo sample conversations are bilingual:** the
sample plays in whichever interface language you picked.

---

## Where is the data?

Short answer: **with you.** DivanAI has no server, no account, no database of its own.

| What | Where it lives | Who can see it |
|---|---|---|
| Your API key | Only in **your browser's** `localStorage` | You. Never sent to any server; even GitHub, which hosts the page, cannot see it |
| Your settings (models, roles, tone, round count) | Same place, your browser | You |
| The last conversation | In the browser session; reload and it comes back | You |
| The topic and text you write | Goes **to the provider you chose** (OpenRouter, Groq, OpenAI…) as a request | That provider, under its own privacy policy |
| The `.md` file you save | On your own computer, wherever you downloaded it | You |
| Cookies, tracking, ads | **None** | — |

> The key lives in your browser: on a shared computer use **Demo** mode when opening DivanAI. If you did
> enter a key, Settings → empty the key field → **Save**; the key is removed from the browser.

**If you want to delete it:** empty the key field in Settings and save (the key is gone), or clear the
site data of this page in your browser (settings go too). There is nothing to delete on a server, because
nothing is held on a server.

**Tasks in Agents mode** are kept only for the open session; closing the page ends them. If you want,
take a backup from the menu: the backup file lands on your computer and belongs to you.

---

## When something is stuck

| Symptom | What to do |
|---|---|
| "… is done for today (free daily quota is used up)" | **Only that seat** stops; the other seats carry on with their own services. If several seats share one key, the table waits and **▶ Continue where you left off** appears |
| `401 invalid api key` | Wrong key: paste it again in Settings, **⇅ Test connection** |
| `404 model not found` | Wrong model id: fix the id on the row (it differs per service) |
| `403 Key limit exceeded` | The key's **spend limit** is zero: `openrouter.ai/settings/keys` → raise Limit |
| A seat went silent | DivanAI switches to a backup and writes `↺ model` in the answer header; the round does not stop |
| Answer cut short | It retries once by itself; if it continues, lower the word limit in Settings or pick a smaller model |
| No image | Rate limit (45 s) or server busy (503); press **Retry** on the card |
| Empty/repeating answer | Free models get crowded; try another free model or move to a paid one |
| The table takes too long | **Stop**, lower **Max rounds**, keep **Stop when saturated** on |
| Settings disappeared | Browser data was cleared: **Load from backup** (keys are entered separately) |

---

## Known limits

- **Demo is not a real model.** The sample texts are fixed and labelled “(Demo)”.
- **Live mode needs the internet.** The keyless demo works without it.
- **Brevity is an upper bound.** A model will not exceed the limit but may write less than you need; for
  a long analysis open a new table focused on one topic.
- **At most 5 seats** — DivanAI knows five providers. Using the same provider in a second seat (e.g. two
  different GPT models) is not possible today.
- **Images vanish on reload**; the conversation text and prompts stay.
- **Backups do not sync between devices automatically** (no account/server, deliberately).

---

## Screens

| Mobile · Mirror | Daily quota |
|---|---|
| ![Mobile](ekranlar/5-mobil.jpg) | ![Quota](ekranlar/7-kota.jpg) |

| Agents · flow and delivery | Mirror: no agenda picker |
|---|---|
| ![Flow](ekranlar/12-ajan-akis.jpg) | ![Mirror](ekranlar/20-ayna-gundem.jpg) |

| Image box: drawn from the agent's text | Connection settings: no card / card required |
|---|---|
| ![Image box](ekranlar/21-gorsel-kutusu.jpg) | ![Connection](ekranlar/8-baglanti.jpg) |

| Paid services in their own layer | Per-seat connection |
|---|---|
| ![Other services](ekranlar/25-diger-servisler.jpg) | ![Seat connection](ekranlar/9-sandalye-baglanti.jpg) |

*DivanAI · one file · no external dependencies.*

---

## Licence

**Apache License 2.0** — full text in `LICENSE`, attribution in `NOTICE`.
The code is free; income comes only from voluntary donations. The 268 English expert entries in Agents
mode come from the [agency-agents](https://github.com/msitarzewski/agency-agents) project (MIT); see
`NOTICE` for details.

## Rename (MASA → DivanAI)

The app was never released as **MASA**; the name became **DivanAI** with version 1.25. For anyone who
tried an earlier version, old records in the browser **migrate by themselves**:

| Old record | New record | What it holds |
|---|---|---|
| `masa_settings_v1` | `divanai_settings_v1` | All settings, provider, **API keys** |
| `masa_session_v1` | `divanai_session_v1` | The unfinished conversation, pause record |
| `masa_req_v1` | `divanai_req_v1` | Today's request counter |
| `masa_quota_v1` | `divanai_quota_v1` | Pause when the quota ran out |

Opening the page once is enough: migration runs a single time and the old record is deleted.
**You do not have to do anything by hand**; your key and settings stay where they are. A `.json`
settings backup you downloaded earlier keeps working too (it is accepted even if the app name inside
says `MASA`).

---

## Security

### Short answer: no server, no account, no data collected

DivanAI is a single file. While it runs it **connects to no server** — neither ours nor anyone else's.
The conversation is created in your browser and stays on screen. Close the page and it ends.

The only exception is the model you choose: the topic you write goes **straight from your browser** to
the service you picked (OpenRouter, Groq, OpenAI…). Nobody sits in between and no copy is made.
Which means: **that service sees what you write.** If you are going to type secrets, ID numbers or
patient data, know that.

### Where does the key live?

In your browser's own vault (localStorage), **on your computer only**. It is never sent anywhere; it only
goes to the address of the provider you chose, in the `Authorization` header.

Two situations to watch:

| Situation | What to do |
|---|---|
| A shared computer | Use **Demo** mode when opening DivanAI; do not enter a key. Or delete the key in Settings when you are done. |
| Browser sync (Chrome/Firefox account) | `localStorage` is not synced by default; if you still do not want the key in a profile tied to a browser account, use a separate profile. |

The key is **never** written to an exported file. When backing up settings the keys are deliberately left
out — even if you share the file, the key is not inside.

### What was checked before release

Before this version went out (34 automated security checks):

- **Running code from a model answer (XSS).** `<script>`, `onerror`, `onload`, `javascript:` links and
  `<iframe>` were hidden inside a model answer. All of them appeared **as text**; none ran.
- **A malicious settings backup.** A broken `.json` backup sent by someone else was used to inject code;
  it did not run.
- **Even when the same answer is kept in memory.** The conversation is stored in the browser; after
  reopening the page the malicious content still did not run.
- **Key leakage.** All network traffic was watched during a live round: the key went only to the chosen
  provider, never appeared in a URL, is not written on the page and is not in the exported file. A “trap
  server” was set up as well: **not a single request** went to it.
- **External resources.** The page has no external script, style, iframe, form or ad.

### Content security policy (CSP)

A **CSP** is set on the page. Because it is a single file, inline code is required; but **no code can be
loaded from outside**: remote scripts, iframes, objects, form submissions and `<base>` hijacking are
closed. So even if an escape hatch were found tomorrow, no outside code could be pulled in. The policy is
delivered with a `<meta>` tag inside the page, since GitHub Pages sends no custom headers.

`Referrer-Policy: no-referrer` is set too: when you click an external link, your page address does not
leak to the other side.

### Local server (`server.py`)

Optional. It listens only on **127.0.0.1** (your own computer) and is unreachable from the network.
Directory listing is off, version info is hidden, broken URLs do not take the server down. You do not
need it for GitHub Pages.

### The one thing left on your side

- When writing the topic, know what is going to that service.
- Do not share your key; close the Settings window before taking a screenshot.
- Only take a suspicious `.json` settings backup from someone you trust.
