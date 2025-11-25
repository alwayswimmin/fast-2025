**High-level overview (2–3 sentences)**  
This talk describes Arbor Biotechnologies’ early-stage gene-editing program aimed at treating Angelman syndrome by unsilencing the normally silent paternal copy of the UBE3A gene in neurons. Using a novel CRISPR-based editor (a type V nuclease) delivered by AAV, Arbor has identified guide RNAs that restore UBE3A protein levels in Angelman patient–derived neurons and normalize an abnormal “hyperexcitable” electrical phenotype in vitro. The work is still preclinical but shows that sequence choice and target location within the UBE3A antisense transcript (UBE3A-ATS) are critical for therapeutic effect.

---

## Speaker introduction

- **Name:** Dr. Rafael (Raph) Benjam  
- **Affiliation:** Arbor Biotechnologies (“Arbor Bio”), a clinical-stage biotechnology company.  
- **Role/Expertise:** Represents Arbor’s research on CRISPR-based gene editing therapies, with a focus on central nervous system (CNS) disorders, including Angelman syndrome.  
- **Company background:**  
  - Arbor is a clinical-stage company developing therapies based on CRISPR gene editing.  
  - They have a liver program for primary hyperoxaluria type 1 (PH1) in Phase 1 clinical trials.  
  - They are building several CNS pipelines at different preclinical stages and are now applying their platform to Angelman syndrome.  

---

## Main sections / topics (in order)

1. Arbor Biotechnologies and its gene-editing platform  
2. CRISPR basics and types of nucleases (Type II vs Type V)  
3. Therapeutic strategy for Angelman syndrome: targeting UBE3A-ATS  
4. Preclinical in vitro screening and guide optimization  
5. Functional rescue of neuronal hyperexcitability (MEA assay)  
6. Summary, implications, and community acknowledgment  

---

### 1. Arbor Biotechnologies and its gene-editing platform

- Arbor is a **clinical-stage CRISPR gene-editing company** with programs in both liver and CNS diseases, including a Phase 1 trial for PH1 and multiple preclinical CNS efforts.  
- The company has discovered and employs **more than 10 distinct gene editors**, including several **Type V nucleases**, which are less commonly used than Cas9 but have properties that may be better suited for certain therapies.  
- Arbor combines its **gene-editing technology** with **AAV (adeno-associated virus) delivery** optimized for the central nervous system, enabling direct targeting of neurons.  
- Their Angelman syndrome program is an application of this platform, using CRISPR-based tools to modulate gene expression in brain cells.  
- The talk marks Arbor’s **public disclosure** that they are actively working on an Angelman syndrome program, moving out of “stealth” mode for this indication.

---

### 2. CRISPR basics and types of nucleases (Type II vs Type V)

- **CRISPR gene editing** uses two main components:  
  - A **Cas protein** (the “molecular scissors”) that cuts DNA at a specific site.  
  - A **guide RNA (gRNA)** that directs the Cas protein to the target DNA sequence.  
- **Type II nucleases**, such as **Cas9**, are the most well-known; Cas9 is widely used in clinical trials and is FDA-approved for sickle cell disease.  
- **Type V nucleases** are less well known but have two key advantages for therapeutics:  
  - They are **smaller**, and their guide RNAs are smaller, which makes it easier to package them into AAV vectors (AAV has a strict size limit).  
  - They create a **staggered cut** in DNA (rather than a blunt cut), which tends to produce **larger deletions**—useful when the goal is to disrupt a long noncoding RNA like UBE3A-ATS.  
- Because of these properties, Type V nucleases are particularly attractive for **CNS gene-editing therapies** where AAV delivery and efficient disruption of long transcripts are crucial.  

---

### 3. Therapeutic strategy for Angelman syndrome: targeting UBE3A-ATS

- In Angelman syndrome, the **maternal copy of UBE3A is lost or nonfunctional**, and the **paternal copy is silenced** in neurons by a long antisense RNA called **UBE3A-ATS**.  
  - **Antisense transcript (ATS):** A long RNA transcribed in the opposite direction that interferes with expression of the main gene (here, UBE3A).  
- Arbor’s strategy is to **disrupt UBE3A-ATS** using their Type V nuclease, thereby **unsilencing the paternal UBE3A** and restoring UBE3A protein in neurons (“pillar 2” / FAST Circle 2 approach).  
- The gene editor (nuclease + guide RNA) is designed to be **packaged into an AAV vector** and delivered as a **one-time treatment**, with the goal of **durable, long-term unsilencing** of paternal UBE3A.  
- Clinical proof-of-concept for this general mechanism (unsilencing paternal UBE3A by targeting UBE3A-ATS) has already been shown by **antisense oligonucleotides (ASOs)** currently in clinical trials, which Arbor uses as a benchmark.  
- Arbor’s relatively **small nuclease** leaves room in the AAV vector for **additional safety features**, such as elements to limit or shut down long-term nuclease expression, which may help manage safety risks.

---

### 4. Preclinical in vitro screening and guide optimization

- The **target region within UBE3A-ATS** is very large (~50,000 DNA bases), so Arbor needed to test many possible guide RNAs to find the most effective ones.  
- They first screened about **300 guides** in an immortalized cell line to eliminate those with poor activity, then tested the best-performing guides in **induced pluripotent stem cell (iPSC)–derived human cortical neurons** from Angelman patients.  
- In these patient-derived neurons, they **ranked guides** based on how well they **restored UBE3A protein expression**, using a **research-grade ASO from the Dindot lab** as a performance benchmark.  
- Through optimization, they improved the **potency of top guide–nuclease combinations by up to 14-fold**, and identified multiple candidates that restored UBE3A protein to **near neurotypical levels**.  
- Data showed:  
  - **Orange bars:** two guide combinations that achieved UBE3A levels similar to neurotypical controls.  
  - **Blue bars:** seven more guides that approached neurotypical levels and matched or exceeded the benchmark ASO’s performance.  

---

### 5. Functional rescue of neuronal hyperexcitability (MEA assay)

- Angelman neurons are reported to show **elevated excitability**—they fire too much and too synchronously—both in vitro (iPSC-derived neurons) and in vivo (animal models), which is thought to relate to **seizure-like activity**.  
- Arbor used a **multi-electrode array (MEA)** system, which measures the electrical activity of neurons in a dish, to quantify this **hyperexcitability** and **synchrony** (how coordinated the firing is across neurons).  
- In their experiments, **untreated Angelman neurons** showed **higher synchrony** than neurotypical neurons, consistent with a hyperexcitable phenotype.  
- After treatment with Arbor’s **top guide–nuclease candidates**, the synchrony of Angelman neurons was **reduced into the neurotypical range**, as quantified by measures like **area under the curve** for synchrony metrics.  
- Importantly, there was a **strong correlation** between the **degree of UBE3A protein restoration** and the **reduction in hyper-synchrony**, indicating that **sequence and target location of the guide** matter and that restoring UBE3A can rescue a functional, seizure-like neuronal phenotype in vitro.

---

### 6. Summary, implications, and community acknowledgment

- Arbor’s approach uses a **Type V CRISPR nuclease delivered by AAV** for a **one-time treatment** aimed at **durable unsilencing of paternal UBE3A** in neurons.  
- Their **top gene editors and guide RNAs** can restore UBE3A protein in Angelman patient–derived neurons to **neurotypical or near-neurotypical levels**, and **reverse hyperexcitability** to a normal range in MEA assays.  
- The work underscores that **guide sequence and exact target location within UBE3A-ATS are critical** for maximizing UBE3A expression and functional rescue, guiding the selection of the best clinical candidate.  
- This is still **early, preclinical work**, but it aligns with and extends the ASO-based strategy by using a potentially **durable gene-editing approach** rather than repeated dosing.  
- Dr. Benjam closed by thanking FAST, Allison, and the Angelman community, emphasizing that their advocacy, participation, and support are central to advancing drug development efforts for Angelman syndrome.