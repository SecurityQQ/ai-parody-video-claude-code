# Not you.

format: social
length: 38
wpm: 150
hook_max: 3
max_shot: 11
facts: facts.md

Promise: Nvidia's keynote opener gets re-cast in front of you, and the new host is Apple from his first word.
Last line: "It's a subscription now."
Strategy: question ladder (a skit). Each beat turns on BUT or SO.
Speakers: DIRECTOR wants a clean opener and wastes no words. JENSEN wants his entrance back and bargains. TIM wants
everyone to have a good morning and sells while he greets.

| # | time | spoken | on screen | visual | sound |
|---|---|---|---|---|---|
| 1 | 0-3.8 | DIRECTOR: "Cut to an interior. Camera follows a mysterious figure..." | NVIDIA'S KEYNOTE OPENER, AFTER THE MODEL INCIDENT · PARODY | Wide glass atrium, green light. A small figure in a black leather jacket crosses left to right. | Low pulse, footsteps on stone |
| 2 | 3.8-6.6 | DIRECTOR: "...before revealing our main character." | PARODY | Camera at floor height tracks black sneakers past a glass wall. | Footsteps closer, pulse rises |
| 3 | 6.6-9 | JENSEN: "Hello, and welcome to N-" | JENSEN HUANG · opener | Dark corridor. The cut-out walks up to the lens; a strip of green light lands on his smiling eyes. | Light swell on the strip. BUT: |
| 4 | 9-11.9 | DIRECTOR: "No, no, no, no, no. Not you." | JENSEN HUANG · ~~opener~~ | His head swaps to the surprised photo. | Music stops dead on the first "no" |
| 5 | 11.9-14.1 | JENSEN: "Is this about the model?" | PARODY | He leans toward the lens. | Room tone only |
| 6 | 14.1-15.9 | DIRECTOR: "It's about the model." | PARODY | He holds still. | Room tone |
| 7 | 15.9-17.3 | JENSEN: "The language model?" | PARODY | Head swaps back to the smile, hopeful. | Room tone |
| 8 | 17.3-18.9 | DIRECTOR: "No." [beat] "Jacket." | PARODY | The smile stays for one beat too long, then he sags. | One beat of silence after "No." SO: |
| 9 | 18.9-21.7 | DIRECTOR: "That's your opener." | PARODY | The jacket lifts off him and flies back. Focus moves to the room behind the glass, where a small figure catches it. | Zip, whoosh, bright music starts on the catch |
| 10 | 21.7-25.5 | TIM: "Good morning! And welcome to Nvidia." | TIM COOK · opener | Daylight corridor, hills outside. The cut-out walks up in a jacket two sizes too big and waves. | Bright music, full |
| 11 | 25.5-31.1 | TIM: "This is the new RTX. It folds." [snap] "The power cable is sold separately." | IT FOLDS · POWER CABLE: SOLD SEPARATELY | He holds up a graphics card; it shuts like a flip phone. Two paper tags pop up beside it. | Snap on the fold, a tick per tag. BUT: |
| 12 | 31.1-35.3 | JENSEN: "Can I have my jacket back?" TIM: "It's a subscription now." | PARODY | Jensen leans in from the left edge in a black T-shirt. Tim does not turn his head. | Music ducks, then back |
| 13 | 35.3-38 | | TIM ~~APPLE~~ NVIDIA · PARODY. Nobody said any of this. | A paper name badge on the daylight plate. Photo credits in small print under it (not counted as reading text). | Last chord rings out |

Three hooks that were kept (the first is used):
1. Type at frame 0, "NVIDIA'S KEYNOTE OPENER, AFTER THE MODEL INCIDENT", over the director's "Cut to an interior."
2. Open on beat 4: "No, no, no, no, no. Not you." over the surprised cut-out, then rewind.
3. Open on the jacket in mid-air with the type "THE JACKET HAS A NEW OWNER".

Crossed out: opening on Tim's "Good morning!" (the first idea; it gives away the turn).

Times above are the budget at 150 words a minute. The real times come from the recorded voices: see `sound/beats.json`.

## As cut

The budget above was written at 150 words a minute before any voice existed. The film as cut, from `sound/beats.json`:
39.7083 s, 72 spoken words, 109 words a minute overall.

| # | time | lines |
|---|---|---|
| 1 | 0.00-3.00 | D1 (first two phrases) |
| 2 | 3.00-5.58 | D1 (last phrase starts) |
| 3 | 5.58-8.08 | J1 |
| 4 | 8.08-10.42 | D2 |
| 5 | 10.85-12.53 | J2 |
| 6 | 12.85-13.87 | D3 |
| 7 | 14.26-15.37 | J3 |
| 8 | 15.88-18.25 | D4, D5 |
| 9 | 18.42-21.21 | D6 |
| 10 | 21.21-24.62 | T1 |
| 11 | 24.62-31.17 | T2, T3 |
| 12 | 31.17-36.42 | J4, T4 |
| 13 | 36.42-39.71 | - |

Changes from the table above, all made in the edit and none in the words: the end card's small print became one credit
line ("Photos (edited): Tessa Bury · Presidential Office, Taiwan · The White House · CC BY"); the lower third under
Tim reads NEW OPENER; four lines were re-recorded slower with a written pause ("Is this... about the model?").

Checker on this file: 0 fail, 2 warn (the hook warning: the first spoken beat ends after 3 s, but the premise is in
type from frame 0; and the end card's reading time, which the cut extends to 3.3 s).
The stop for approval before any voice or picture was passed without a person (the request was a /goal).
