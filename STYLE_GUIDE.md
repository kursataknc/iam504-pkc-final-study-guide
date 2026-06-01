# Solution Style Guide — IAM504 Public Key Cryptography (Boneh–Shoup)

You are writing exam-prep solutions that MUST match the language and structure of the
course recitation. Study these conventions and follow them exactly.

## The recitation's proof grammar (use this skeleton for every reduction)
1. **Open with the idea.** One short paragraph in plain language: "The idea is simple. We
   show that an efficient adversary 𝒜 that breaks <scheme/property> implies an efficient
   adversary ℬ (an *elementary wrapper* around 𝒜) that breaks <hard assumption>."
2. **Construct ℬ explicitly.** State what challenge ℬ receives, how it builds the inputs it
   hands to 𝒜 (public key, ciphertexts, oracle responses), and how it uses 𝒜's output.
3. **Case analysis / game hops.** When the challenge is "real vs. random", analyze the two
   cases: in the "real/DH" case ℬ perfectly simulates the true game; in the "random" case
   𝒜's view is independent of the hidden bit so its advantage is 0 (or it's a perfect guess).
4. **Conclude with a concrete bound**, e.g.
   `SSadv[𝒜, E] ≤ 2·(1/q + DDHadv[ℬ, G])`, and tie advantages together explicitly.

## Notation (use these exact advantage names)
- `DLadv[B,G]`, `CDHadv[B,G]`, `DDHadv[B,G]`, `ICDHadv`, `coCDHadv`
- `Distadv[A,D,R]` (distinguishing advantage between distributions D and R)
- `SSadv[A,E]` (semantic security), `CPAadv[A,E]`, `1CCAadv[A,E]`, `CCAadv[A,E]`
- `PRFadv`, `wPRFadv`, `PRFroadv` (PRF in random-oracle model)
- `CRadv[A,H]` (collision resistance), `SIGadv`, `SIGroadv`, `SELadv`, `sbSIGadv`
- Bit-guessing vs. real advantage: `SSadv = 2·SSadv*` etc., used as in the recitation.
- Groups: G cyclic of prime order q, generator g; elements written g^α. Use \mathbb{G},
  \mathbb{Z}_q in LaTeX.

## Tone & rigor
- Full rigor: explicit adversary construction, every simulation step, the final inequality.
- But begin each solution with a 1–2 sentence intuition ("what's really going on").
- Mirror phrases the recitation uses: "elementary wrapper", "perfectly simulates",
  "is uniformly distributed over … independently of b", "by the Difference Lemma", "by a
  standard hybrid argument", "as required."
- When an exercise says "show an attack", give the explicit adversary and show its
  advantage is 1 (or as required), no reduction needed.

## Output format — STRICT (so fragments concatenate into one HTML file)
For EACH problem, emit exactly one `<section>` with this structure (no <html>/<head>/<body>):

```html
<section class="problem" id="ex-CH-NN" data-ch="CH">
  <h3 class="ptitle"><span class="pnum">CH.NN</span> <span class="pname">(Short name)</span></h3>
  <div class="statement">
    <p>Faithful restatement of the problem (paraphrase is fine; keep all given formulas).</p>
  </div>
  <button class="toggle" type="button">Show solution</button>
  <div class="solution">
    <h4>Idea</h4>
    <p>...one short intuition paragraph...</p>
    <h4>Solution</h4>
    <p>...full rigorous solution, multiple paragraphs...</p>
  </div>
</section>
```

### Math rules (MathJax is loaded in the master file)
- Inline math: `\( ... \)`   Display math: `\[ ... \]`
- Do NOT use $...$ (it's disabled). Use \( \) and \[ \].
- Escape nothing else; write real `<`, `>` only outside math — inside math they're fine in \(\).
- Use `\mathbb{G}, \mathbb{Z}_q, \alpha, \beta, \leftarrow, \xleftarrow{R}` etc.
- For "chosen at random" use `\xleftarrow{\$}` or write "\(x \stackrel{R}{\leftarrow} S\)".

### IDs: id="ex-10-1" for problem 10.1, id="ex-12-23" for 12.23, etc. data-ch is the chapter number.

Produce the sections in ascending problem order, concatenated, nothing else.
