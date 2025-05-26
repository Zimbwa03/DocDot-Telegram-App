import sqlite3
import json

def add_batch_questions(questions_list):
    """
    Add multiple questions to the database.
    Each question should be a dictionary with keys:
    - question: str
    - answer: bool
    - explanation: str
    - ai_explanation: str
    - references: dict
    - category: str
    """
    conn = sqlite3.connect('questions.db')
    cursor = conn.cursor()

    for q in questions_list:
        try:
            cursor.execute('''
                INSERT INTO questions
                (question, answer, explanation, ai_explanation, reference_json, category)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (
                q['question'],
                q['answer'],
                q['explanation'],
                q.get('ai_explanation', ''),
                json.dumps(q.get('references', {})),
                q['category']
            ))
            print(f"Added question: {q['question'][:50]}...")
        except Exception as e:
            print(f"Error adding question: {e}")

    conn.commit()
    conn.close()

# Example usage:
if __name__ == "__main__":
    # Example batch of questions
    questions = [
    {
    "question": "Reticular fibers are composed mainly of collagen type III.",
    "answer": True,
    "explanation": "Reticular fibers primarily consist of type III collagen forming delicate networks in lymphoid tissues.",
    "ai_explanation": "Their fine branching structure supports cells in lymph nodes, spleen, and bone marrow.",
    "references": {
      "Ross & Pawlina": "Chapter 5, pp. 114",
      "Junqueira’s Basic Histology": "Chapter 6, pp. 125",
      "Wheater’s Functional Histology": "Chapter 4, pp. 64"
    },
    "category": "Histology and Embryology"
  },

  {
    "question": "Collagen fibers provide tensile strength to connective tissues.",
    "answer": True,
    "explanation": "Collagen fibers resist stretching forces, maintaining tissue integrity under tension.",
    "ai_explanation": "The molecular structure and cross-linking of collagen fibrils create strong, flexible fibers.",
    "references": {
      "Ross & Pawlina": "Chapter 5, pp. 112-113",
      "Junqueira’s Basic Histology": "Chapter 6, pp. 124",
      "Wheater’s Functional Histology": "Chapter 4, pp. 64"
    },
    "category": "Histology and Embryology"
  },
  {
    "question": "Mesenchyme is an example of dense connective tissue.",
    "answer": False,
    "explanation": "Mesenchyme is a loosely arranged embryonic connective tissue, not dense connective tissue.",
    "ai_explanation": "Dense connective tissue contains tightly packed collagen fibers, whereas mesenchyme is loosely arranged with abundant ground substance.",
    "references": {
      "Ross & Pawlina": "Chapter 5, pp. 105-106",
      "Junqueira’s Basic Histology": "Chapter 6, pp. 121",
      "Wheater’s Functional Histology": "Chapter 4, pp. 60-61"
    },
    "category": "Histology and Embryology"
  },
  {
    "question": "Fibroblasts are capable of phagocytosis.",
    "answer": False,
    "explanation": "Fibroblasts generally do not perform phagocytosis; this function is mainly carried out by macrophages.",
    "ai_explanation": "Phagocytic activity is a specialized function of immune cells like macrophages, not fibroblasts involved in matrix production.",
    "references": {
      "Ross & Pawlina": "Chapter 5, pp. 114",
      "Junqueira’s Basic Histology": "Chapter 6, pp. 124",
      "Wheater’s Functional Histology": "Chapter 4, pp. 64"
    },
    "category": "Histology and Embryology"
  },
  {
    "question": "Mesenchymal cells have abundant mitochondria due to high energy demands.",
    "answer": True,
    "explanation": "The high metabolic and synthetic activity of mesenchymal cells requires numerous mitochondria.",
    "ai_explanation": "Mitochondria supply ATP to support active proliferation and matrix synthesis in mesenchymal cells.",
    "references": {
      "Ross & Pawlina": "Chapter 5, pp. 107",
      "Junqueira’s Basic Histology": "Chapter 6, pp. 121",
      "Wheater’s Functional Histology": "Chapter 4, pp. 61"
    },
    "category": "Histology and Embryology"
  },
  {
    "question": "Mesenchyme forms the basis for the development of blood vessels.",
    "answer": True,
    "explanation": "Mesenchymal cells differentiate into endothelial cells that line blood vessels during angiogenesis.",
    "ai_explanation": "Vasculogenesis and angiogenesis involve mesenchymal-derived cells forming the vascular endothelium.",
    "references": {
      "Ross & Pawlina": "Chapter 5, pp. 109",
      "Junqueira’s Basic Histology": "Chapter 6, pp. 122",
      "Wheater’s Functional Histology": "Chapter 4, pp. 62"
    },
    "category": "Histology and Embryology"
  },
  {
    "question": "Mesenchyme cells secrete large amounts of extracellular matrix.",
    "answer": True,
    "explanation": "Mesenchymal cells produce ground substance and fibers forming the extracellular matrix essential for tissue structure.",
    "ai_explanation": "The extracellular matrix secreted by mesenchymal cells supports cell adhesion, migration, and differentiation.",
    "references": {
      "Ross & Pawlina": "Chapter 5, pp. 107-108",
      "Junqueira’s Basic Histology": "Chapter 6, pp. 121-122",
      "Wheater’s Functional Histology": "Chapter 4, pp. 61"
    },
    "category": "Histology and Embryology"
  },
  {
    "question": "Mesenchyme is considered a type of specialized connective tissue.",
    "answer": False,
    "explanation": "Mesenchyme is classified as embryonic connective tissue, not specialized connective tissue.",
    "ai_explanation": "Specialized connective tissues include cartilage, bone, and blood, which arise from mesenchyme but are distinct in structure and function.",
    "references": {
      "Ross & Pawlina": "Chapter 5, pp. 105",
      "Junqueira’s Basic Histology": "Chapter 6, pp. 120",
      "Wheater’s Functional Histology": "Chapter 4, pp. 60"
    },
    "category": "Histology and Embryology"
  },
  {
    "question": "Goblet cells in the respiratory tract secrete mucus to trap inhaled particles.",
    "answer": True,
    "explanation": "Goblet cells are unicellular glands producing mucus to lubricate and protect the airway lining.",
    "ai_explanation": "Goblet cells secrete mucins that hydrate to form mucus, trapping dust, microbes, and pollutants. This mucus is moved by cilia toward the pharynx, clearing contaminants. Dysfunction or excessive mucus secretion can contribute to diseases like asthma and chronic bronchitis.",
    "references": {
      "Junqueira’s Histology": "Chapter 5, pp. 95–97",
      "Wheater’s Functional Histology": "Chapter 11, pp. 232–234"
    },
    "category": "Histology and Embryology"
  },
  {
    "question": "The paraxial mesoderm does not contribute to the formation of the kidneys.",
    "answer": True,
    "explanation": "Kidneys develop mainly from intermediate mesoderm, not paraxial mesoderm.",
    "ai_explanation": "Intermediate mesoderm differentiates into the urogenital ridge, which gives rise to kidneys and gonads. The paraxial mesoderm forms somites contributing to axial skeleton and musculature. Understanding mesodermal origins is vital for developmental biology and congenital anomaly insights.",
    "references": {
      "Langman’s Medical Embryology": "Chapter 6, pp. 98–100",
      "The Developing Human": "Chapter 8, pp. 120–122"
    },
    "category": "Histology and Embryology"
  },
  {
    "question": "Melanocytes are derived from neural crest cells.",
    "answer": True,
    "explanation": "Melanocytes originate from the neural crest and migrate to the epidermis.",
    "ai_explanation": "Neural crest cells are multipotent and migrate extensively during development. Melanocytes produce melanin pigment protecting skin from UV radiation. Defects in neural crest migration or function cause pigmentation disorders such as vitiligo or piebaldism.",
    "references": {
      "Junqueira’s Histology": "Chapter 6, pp. 105–107",
      "Ross & Pawlina": "Chapter 6, pp. 176–178"
    },
    "category": "Histology and Embryology"
  },
  {
    "question": "The visceral layer of the serous pericardium is also known as the epicardium.",
    "answer": True,
    "explanation": "The epicardium is the outer layer of the heart wall derived from the visceral pericardium.",
    "ai_explanation": "The epicardium consists of a mesothelial layer and underlying connective tissue. It protects the heart and contains coronary vessels and nerves. It also participates in heart development and repair mechanisms. Inflammation can cause pericarditis, affecting cardiac function.",
    "references": {
      "Junqueira’s Histology": "Chapter 14, pp. 260–262",
      "Ross & Pawlina": "Chapter 14, pp. 310–312"
    },
    "category": "Histology and Embryology"
  },
  {
    "question": "The primary palate forms before the secondary palate during embryonic development.",
    "answer": True,
    "explanation": "The primary palate forms around week 6, preceding the fusion of the secondary palate.",
    "ai_explanation": "The primary palate arises from the intermaxillary segment and contributes to the upper lip and premaxillary maxilla. The secondary palate forms later from palatal shelves and separates the oral and nasal cavities. Failure of fusion causes cleft palate and associated feeding and speech problems.",
    "references": {
      "Langman’s Medical Embryology": "Chapter 10, pp. 150–152",
      "Before We Are Born": "Chapter 10, pp. 160–162"
    },
    "category": "Histology and Embryology"
  },
  {
    "question": "The adrenal cortex is derived from mesoderm, while the adrenal medulla originates from neural crest cells.",
    "answer": True,
    "explanation": "These two parts of the adrenal gland have distinct embryological origins.",
    "ai_explanation": "The cortex arises from intermediate mesoderm and produces steroid hormones. The medulla, from neural crest-derived chromaffin cells, secretes catecholamines like adrenaline. Disruptions in development can cause congenital adrenal hyperplasia or pheochromocytomas.",
    "references": {
      "Langman’s Medical Embryology": "Chapter 12, pp. 170–172",
      "Junqueira’s Histology": "Chapter 16, pp. 255–257"
    },
    "category": "Histology and Embryology"
  },
  {
    "question": "Osteoblasts are derived from mesenchymal stem cells.",
    "answer": True,
    "explanation": "Osteoblasts originate from mesenchymal progenitors and are responsible for bone formation.",
    "ai_explanation": "Mesenchymal stem cells differentiate into osteoblasts that secrete collagen and matrix for bone mineralization. They also regulate osteoclast activity. Understanding this lineage is important in bone diseases like osteoporosis and fractures healing.",
    "references": {
      "Junqueira’s Histology": "Chapter 11, pp. 190–192",
      "Ross & Pawlina": "Chapter 11, pp. 260–262"
    },
    "category": "Histology and Embryology"
  },
  {
    "question": "The thyroid gland originates from endodermal tissue at the base of the tongue.",
    "answer": True,
    "explanation": "The thyroid arises from a median endodermal thickening known as the thyroid diverticulum.",
    "ai_explanation": "The diverticulum descends to the neck, forming the thyroid gland. The thyroglossal duct connects the thyroid to the tongue temporarily. Persistence of this duct can cause thyroglossal cysts. Proper thyroid development is essential for metabolism regulation.",
    "references": {
      "Langman’s Medical Embryology": "Chapter 11, pp. 160–162",
      "Junqueira’s Histology": "Chapter 17, pp. 270–272"
    },
    "category": "Histology and Embryology"
  },
  {
    "question": "The dorsal root ganglia are derived from neural crest cells.",
    "answer": True,
    "explanation": "Neural crest cells migrate and differentiate into sensory neurons of dorsal root ganglia.",
    "ai_explanation": "The dorsal root ganglia contain the cell bodies of sensory neurons that transmit information to the CNS. Neural crest cells contribute to peripheral nervous system formation. Defects in this process can cause sensory neuropathies and developmental disorders.",
    "references": {
      "Langman’s Medical Embryology": "Chapter 5, pp. 65–67",
      "Ross & Pawlina": "Chapter 9, pp. 220–222"
    },
    "category": "Histology and Embryology"
  },
  {
    "question": "Mesenchymal cells have the ability to differentiate into osteoblasts.",
    "answer": True,
    "explanation": "Mesenchymal stem cells can differentiate into osteoblasts, which are bone-forming cells.",
    "ai_explanation": "Osteoblasts originate from mesenchymal progenitor cells during bone formation and remodeling.",
    "references": {
      "Ross & Pawlina": "Chapter 5, pp. 111",
      "Junqueira’s Basic Histology": "Chapter 6, pp. 128",
      "Wheater’s Functional Histology": "Chapter 4, pp. 65"
    },
    "category": "Histology and Embryology"
  },
  {
    "question": "Fibroblasts play a role in wound healing.",
    "answer": True,
    "explanation": "Fibroblasts migrate to injury sites to produce extracellular matrix and collagen necessary for tissue repair.",
    "ai_explanation": "Fibroblast proliferation and matrix production are critical for the formation of granulation tissue in wound healing.",
    "references": {
      "Ross & Pawlina": "Chapter 5, pp. 113",
      "Junqueira’s Basic Histology": "Chapter 6, pp. 125",
      "Wheater’s Functional Histology": "Chapter 4, pp. 65"
    },
    "category": "Histology and Embryology"
  },
  {
    "question": "Macrophages are the primary cells responsible for collagen synthesis.",
    "answer": False,
    "explanation": "Collagen synthesis is mainly performed by fibroblasts, not macrophages.",
    "ai_explanation": "Macrophages are phagocytic cells involved in immune response, while fibroblasts synthesize collagen for connective tissue.",
    "references": {
      "Ross & Pawlina": "Chapter 5, pp. 114",
      "Junqueira’s Basic Histology": "Chapter 6, pp. 124",
      "Wheater’s Functional Histology": "Chapter 4, pp. 64"
    },
    "category": "Histology and Embryology"
  },
  {
    "question": "Mesenchyme lacks a well-developed basement membrane.",
    "answer": True,
    "explanation": "Mesenchymal cells are loosely organized and do not have a distinct basement membrane like epithelial cells.",
    "ai_explanation": "The absence of a basement membrane in mesenchyme allows for cell migration and differentiation during development.",
    "references": {
      "Ross & Pawlina": "Chapter 5, pp. 109",
      "Junqueira’s Basic Histology": "Chapter 6, pp. 121",
      "Wheater’s Functional Histology": "Chapter 4, pp. 61"
    },
    "category": "Histology and Embryology"
  },
  {
    "question": "Elastic fibers can stretch and return to their original shape.",
    "answer": True,
    "explanation": "Elastic fibers provide elasticity allowing tissues to resume shape after stretching or contracting.",
    "ai_explanation": "The elastin core in elastic fibers allows for reversible stretching in tissues such as lungs and arteries.",
    "references": {
      "Ross & Pawlina": "Chapter 5, pp. 113",
      "Junqueira’s Basic Histology": "Chapter 6, pp. 124",
      "Wheater’s Functional Histology": "Chapter 4, pp. 64"
    },
    "category": "Histology and Embryology"
  },
  {
    "question": "Mast cells release histamine during allergic reactions.",
    "answer": True,
    "explanation": "Mast cells contain granules rich in histamine which are released during hypersensitivity reactions.",
    "ai_explanation": "Histamine release from mast cells causes vasodilation and increased vascular permeability during allergic responses.",
    "references": {
      "Ross & Pawlina": "Chapter 5, pp. 116",
      "Junqueira’s Basic Histology": "Chapter 6, pp. 127",
      "Wheater’s Functional Histology": "Chapter 4, pp. 67"
    },
    "category": "Histology and Embryology"
  },
  {
    "question": "Ground substance is stained strongly by hematoxylin in H&E staining.",
    "answer": False,
    "explanation": "Ground substance is usually unstained or faintly stained in H&E because it is mainly composed of hydrophilic molecules that do not bind hematoxylin strongly.",
    "ai_explanation": "Hematoxylin stains acidic structures like nuclei; ground substance is mostly extracellular matrix and appears pale or clear.",
    "references": {
      "Ross & Pawlina": "Chapter 5, pp. 110",
      "Junqueira’s Basic Histology": "Chapter 6, pp. 126",
      "Wheater’s Functional Histology": "Chapter 4, pp. 63"
    },
    "category": "Histology and Embryology"
  },
  {
    "question": "Fibroblasts have a spindle-shaped morphology.",
    "answer": True,
    "explanation": "Fibroblasts are typically elongated and spindle-shaped, facilitating matrix production and tissue repair.",
    "ai_explanation": "Their shape supports extensive cytoplasmic processes for extracellular matrix secretion.",
    "references": {
      "Ross & Pawlina": "Chapter 5, pp. 111",
      "Junqueira’s Basic Histology": "Chapter 6, pp. 123",
      "Wheater’s Functional Histology": "Chapter 4, pp. 63"
    },
    "category": "Histology and Embryology"
  },
  {
    "question": "Mesenchymal cells are connected by tight junctions.",
    "answer": False,
    "explanation": "Mesenchymal cells do not typically form tight junctions; such junctions are characteristic of epithelial cells.",
    "ai_explanation": "Loose organization and migratory capacity of mesenchymal cells prevent tight junction formation.",
    "references": {
      "Ross & Pawlina": "Chapter 5, pp. 109",
      "Junqueira’s Basic Histology": "Chapter 6, pp. 122",
      "Wheater’s Functional Histology": "Chapter 4, pp. 62"
    },
    "category": "Histology and Embryology"
  },
  {
    "question": "Reticular fibers form the structural framework of lymphoid organs.",
    "answer": True,
    "explanation": "Reticular fibers create a supportive meshwork in lymph nodes, spleen, and bone marrow.",
    "ai_explanation": "Their fine collagen III fibers provide structural support while allowing cell movement within lymphoid tissues.",
    "references": {
      "Ross & Pawlina": "Chapter 5, pp. 114",
      "Junqueira’s Basic Histology": "Chapter 6, pp. 125",
      "Wheater’s Functional Histology": "Chapter 4, pp. 64"
    },
    "category": "Histology and Embryology"
  },
  {
    "question": "Mesenchyme is rich in collagen fibers.",
    "answer": False,
    "explanation": "Mesenchyme contains few collagen fibers; it is mostly composed of ground substance and loosely arranged cells.",
    "ai_explanation": "The immature extracellular matrix of mesenchyme has limited collagen, allowing flexibility during development.",
    "references": {
      "Ross & Pawlina": "Chapter 5, pp. 106",
      "Junqueira’s Basic Histology": "Chapter 6, pp. 121",
      "Wheater’s Functional Histology": "Chapter 4, pp. 61"
    },
    "category": "Histology and Embryology"
  },
  {
    "question": "Collagen fibers are stained pink by eosin in H&E staining.",
    "answer": True,
    "explanation": "Collagen fibers bind eosin and stain pink in hematoxylin and eosin preparations.",
    "ai_explanation": "The eosinophilic staining highlights the collagenous extracellular matrix in connective tissues.",
    "references": {
      "Ross & Pawlina": "Chapter 5, pp. 112",
      "Junqueira’s Basic Histology": "Chapter 6, pp. 124",
      "Wheater’s Functional Histology": "Chapter 4, pp. 64"
    },
    "category": "Histology and Embryology"
  },
  {
    "question": "Fibroblasts can transform into myofibroblasts during wound healing.",
    "answer": True,
    "explanation": "Fibroblasts differentiate into myofibroblasts that have contractile properties to aid wound contraction.",
    "ai_explanation": "Myofibroblasts express actin and contribute to tissue remodeling and closure of wounds.",
    "references": {
      "Ross & Pawlina": "Chapter 5, pp. 113",
      "Junqueira’s Basic Histology": "Chapter 6, pp. 125",
      "Wheater’s Functional Histology": "Chapter 4, pp. 65"
    },
    "category": "Histology and Embryology"
  },
  {
    "question": "Mesenchymal cells give rise to skeletal muscle cells.",
    "answer": True,
    "explanation": "Mesenchymal stem cells differentiate into myoblasts which fuse to form skeletal muscle fibers.",
    "ai_explanation": "During development, mesenchymal progenitors commit to myogenic lineage forming skeletal muscle tissue.",
    "references": {
      "Ross & Pawlina": "Chapter 5, pp. 109",
      "Junqueira’s Basic Histology": "Chapter 6, pp. 127",
      "Wheater’s Functional Histology": "Chapter 4, pp. 62"
    },
    "category": "Histology and Embryology"
  },
  {
    "question": "Adipose tissue is a type of specialized connective tissue.",
    "answer": True,
    "explanation": "Adipose tissue is classified as specialized connective tissue due to its distinct functions in energy storage and insulation.",
    "ai_explanation": "It contains adipocytes that store fat and serves metabolic and cushioning roles in the body.",
    "references": {
      "Ross & Pawlina": "Chapter 5, pp. 130",
      "Junqueira’s Basic Histology": "Chapter 6, pp. 131",
      "Wheater’s Functional Histology": "Chapter 4, pp. 66"
    },
    "category": "Histology and Embryology"
  },
  {
    "question": "Mesenchyme is present throughout adult connective tissues.",
    "answer": False,
    "explanation": "Mesenchyme is primarily embryonic and not found in adult connective tissue.",
    "ai_explanation": "In adults, mesenchymal stem cells reside in specific niches but mesenchyme as a tissue is embryonic only.",
    "references": {
      "Ross & Pawlina": "Chapter 5, pp. 106",
      "Junqueira’s Basic Histology": "Chapter 6, pp. 120",
      "Wheater’s Functional Histology": "Chapter 4, pp. 61"
    },
    "category": "Histology and Embryology"
  },
  {
    "question": "Fibroblasts secrete elastin fibers.",
    "answer": True,
    "explanation": "Fibroblasts synthesize and secrete elastin, which forms elastic fibers in connective tissue.",
    "ai_explanation": "Elastin production by fibroblasts contributes to the elasticity of skin, lungs, and blood vessels.",
    "references": {
      "Ross & Pawlina": "Chapter 5, pp. 113",
      "Junqueira’s Basic Histology": "Chapter 6, pp. 124",
      "Wheater’s Functional Histology": "Chapter 4, pp. 64"
    },
    "category": "Histology and Embryology"
  },
  {
    "question": "Macrophages originate from monocytes in the bloodstream.",
    "answer": True,
    "explanation": "Monocytes in the blood migrate into tissues and differentiate into macrophages.",
    "ai_explanation": "This differentiation enables macrophages to perform phagocytosis and immune surveillance in tissues.",
    "references": {
      "Ross & Pawlina": "Chapter 5, pp. 115",
      "Junqueira’s Basic Histology": "Chapter 6, pp. 128",
      "Wheater’s Functional Histology": "Chapter 4, pp. 66"
    },
    "category": "Histology and Embryology"
  },

{
    "question": "The syncytiotrophoblast invades the maternal endometrium and contributes to hormone secretion.",
    "answer": True,
    "explanation": "The syncytiotrophoblast, a multinucleated outer layer of the trophoblast, invades the endometrium and secretes hCG.",
    "ai_explanation": "The syncytiotrophoblast facilitates implantation by penetrating the maternal endometrium. It produces hCG, essential for maintaining the corpus luteum in early pregnancy. Its invasive role also contributes to maternal blood space formation in the placenta. Impaired invasion is linked to preeclampsia.",
    "references": {
      "Langman’s Medical Embryology": "Chapter 3, pp. 41–43",
      "Before We Are Born": "Chapter 3, pp. 38–40"
    },
    "category": "Histology and Embryology"
  },
  {
    "question": "Stratified squamous epithelium is typically found lining the small intestine.",
    "answer": False,
    "explanation": "The small intestine is lined by simple columnar epithelium with goblet cells, not stratified squamous epithelium.",
    "ai_explanation": "The lining of the small intestine is designed for absorption and includes enterocytes and goblet cells within a simple columnar epithelium. Stratified squamous epithelium, suited for abrasion, is found in the esophagus and skin. Misunderstanding epithelial distribution can confuse diagnostics in GI pathology.",
    "references": {
      "Ross & Pawlina": "Chapter 15, pp. 348–350",
      "Junqueira’s Histology": "Chapter 15, pp. 240–242"
    },
    "category": "Histology and Embryology"
  },
  {
    "question": "The cloaca is a common cavity for the urinary and gastrointestinal tracts in early development.",
    "answer": True,
    "explanation": "The cloaca is a transient embryonic structure that later divides into the rectum and urogenital sinus.",
    "ai_explanation": "The cloaca is a shared chamber into which the hindgut and allantois empty. It eventually partitions into the rectum and urogenital sinus via the urorectal septum. Errors in this division can cause anorectal malformations or persistent cloaca, especially in females.",
    "references": {
      "Langman’s Medical Embryology": "Chapter 14, pp. 203–205",
      "The Developing Human": "Chapter 15, pp. 220–222"
    },
    "category": "Histology and Embryology"
  },
  {
    "question": "Chondrocytes are responsible for bone resorption.",
    "answer": False,
    "explanation": "Chondrocytes maintain cartilage, while osteoclasts are responsible for bone resorption.",
    "ai_explanation": "Chondrocytes secrete the extracellular matrix of cartilage and help maintain its structure. Bone resorption is performed by osteoclasts—multinucleated cells derived from monocytes. Confusing their roles may lead to misunderstandings in skeletal pathologies like osteoarthritis versus osteoporosis.",
    "references": {
      "Junqueira’s Histology": "Chapter 8, pp. 155–157",
      "Wheater’s Functional Histology": "Chapter 8, pp. 168–170"
    },
    "category": "Histology and Embryology"
  },
  {
    "question": "Cilia are present on the surface of pseudostratified columnar epithelium in the respiratory tract.",
    "answer": True,
    "explanation": "Pseudostratified columnar epithelium of the respiratory tract contains motile cilia that help move mucus.",
    "ai_explanation": "This epithelium is specialized for mucociliary clearance. Cilia beat rhythmically to move mucus, trapping inhaled particles and pathogens. This defense is compromised in conditions like primary ciliary dyskinesia (Kartagener syndrome), leading to chronic respiratory infections.",
    "references": {
      "Ross & Pawlina": "Chapter 5, pp. 124–126",
      "Junqueira’s Histology": "Chapter 5, pp. 100–102"
    },
    "category": "Histology and Embryology"
  },
  {
    "question": "Hassall’s corpuscles are found in the cortex of the thymus.",
    "answer": False,
    "explanation": "Hassall’s corpuscles are found in the medulla of the thymus, not the cortex.",
    "ai_explanation": "Hassall’s corpuscles are concentric structures in the thymic medulla formed by epithelial reticular cells. They are thought to aid in T-cell maturation and deletion of autoreactive T-cells. Their presence is diagnostic of thymic tissue in histologic sections.",
    "references": {
      "Junqueira’s Histology": "Chapter 14, pp. 265–266",
      "Wheater’s Functional Histology": "Chapter 9, pp. 188–189"
    },
    "category": "Histology and Embryology"
  },
  {
    "question": "The notochord induces the overlying ectoderm to form the neural plate.",
    "answer": True,
    "explanation": "The notochord secretes signaling molecules that direct ectodermal cells to form the neural plate.",
    "ai_explanation": "This inductive interaction is crucial for neurulation. The notochord expresses factors like Sonic Hedgehog (Shh) that direct neural ectoderm development. Disruption in this signaling pathway can lead to neural tube defects like spina bifida or anencephaly.",
    "references": {
      "Langman’s Medical Embryology": "Chapter 5, pp. 68–70",
      "The Developing Human": "Chapter 6, pp. 86–88"
    },
    "category": "Histology and Embryology"
  },
  {
    "question": "Columnar epithelial cells are typically found in the epidermis of the skin.",
    "answer": False,
    "explanation": "The epidermis is composed of keratinized stratified squamous epithelium, not columnar cells.",
    "ai_explanation": "The skin's outer barrier consists of stratified squamous epithelium to resist abrasion. Columnar epithelium is specialized for absorption and secretion, as found in the intestines. Misidentifying epithelial types can impair understanding of pathology and tissue adaptation.",
    "references": {
      "Wheater’s Functional Histology": "Chapter 3, pp. 46–48",
      "Ross & Pawlina": "Chapter 4, pp. 98–100"
    },
    "category": "Histology and Embryology"
  },
  {
    "question": "Oligodendrocytes myelinate axons in the central nervous system.",
    "answer": True,
    "explanation": "Oligodendrocytes are glial cells that form myelin in the CNS.",
    "ai_explanation": "Each oligodendrocyte can extend processes to myelinate several axons, enhancing conduction speed. Demyelination by immune attack in diseases like multiple sclerosis affects CNS function, highlighting their importance. This is distinct from Schwann cells in the PNS, which myelinate a single axon.",
    "references": {
      "Junqueira’s Histology": "Chapter 9, pp. 180–182",
      "Ross & Pawlina": "Chapter 9, pp. 216–218"
    },
    "category": "Histology and Embryology"
  },
  {
    "question": "Meckel’s diverticulum results from incomplete obliteration of the vitelline duct.",
    "answer": True,
    "explanation": "Meckel’s diverticulum is a remnant of the vitelline duct, which normally disappears during fetal development.",
    "ai_explanation": "It can contain ectopic gastric or pancreatic tissue, causing ulceration or bleeding. Located in the ileum, it's the most common congenital anomaly of the GI tract. Awareness is important in pediatric patients presenting with painless rectal bleeding.",
    "references": {
      "Before We Are Born": "Chapter 15, pp. 220–221",
      "Langman’s Medical Embryology": "Chapter 15, pp. 210–212"
    },
    "category": "Histology and Embryology"
  },
  {
    "question": "Fibroblasts contain abundant rough endoplasmic reticulum due to active protein synthesis.",
    "answer": True,
    "explanation": "Fibroblasts synthesize collagen and other extracellular matrix proteins, requiring extensive rough ER.",
    "ai_explanation": "The rough ER supports production and secretion of collagen and glycoproteins necessary for connective tissue structure.",
    "references": {
      "Junqueira’s Basic Histology": "Chapter 6, pp. 123-124",
      "Ross & Pawlina": "Chapter 5, pp. 111-112",
      "Wheater’s Functional Histology": "Chapter 4, pp. 63-64"
    },
    "category": "Histology and Embryology"
  },
  {
    "question": "Mast cells derive from hematopoietic stem cells in the bone marrow.",
    "answer": True,
    "explanation": "Mast cells originate from bone marrow progenitors and mature in peripheral tissues.",
    "ai_explanation": "Their bone marrow origin is common to other immune cells, and they participate in allergic and inflammatory responses.",
    "references": {
      "Ross & Pawlina": "Chapter 5, pp. 116",
      "Junqueira’s Basic Histology": "Chapter 6, pp. 127",
      "Wheater’s Functional Histology": "Chapter 4, pp. 67"
    },
    "category": "Histology and Embryology"
  },
  {
    "question": "Reticular fibers are composed primarily of collagen type III.",
    "answer": True,
    "explanation": "Reticular fibers are mainly made up of type III collagen, providing a delicate supporting meshwork.",
    "ai_explanation": "This type of collagen forms fine fibers in lymphoid organs and bone marrow supporting cell attachment.",
    "references": {
      "Ross & Pawlina": "Chapter 5, pp. 114",
      "Junqueira’s Basic Histology": "Chapter 6, pp. 125",
      "Wheater’s Functional Histology": "Chapter 4, pp. 64"
    },
    "category": "Histology and Embryology"
  },
  {
    "question": "Adipocytes store triglycerides as their primary function.",
    "answer": True,
    "explanation": "Adipocytes specialize in storing energy in the form of triglycerides within large lipid droplets.",
    "ai_explanation": "This energy reserve can be mobilized during periods of fasting or increased energy demand.",
    "references": {
      "Ross & Pawlina": "Chapter 5, pp. 130",
      "Junqueira’s Basic Histology": "Chapter 6, pp. 131",
      "Wheater’s Functional Histology": "Chapter 4, pp. 66"
    },
    "category": "Histology and Embryology"
  },
  {
    "question": "Collagen fibers have high tensile strength due to their triple helix structure.",
    "answer": True,
    "explanation": "Collagen’s triple helical arrangement provides great mechanical strength to connective tissues.",
    "ai_explanation": "This molecular structure resists stretching forces, supporting tissue integrity.",
    "references": {
      "Ross & Pawlina": "Chapter 5, pp. 112",
      "Junqueira’s Basic Histology": "Chapter 6, pp. 124",
      "Wheater’s Functional Histology": "Chapter 4, pp. 64"
    },
    "category": "Histology and Embryology"
  },
  {
    "question": "Fibroblasts are stationary cells that do not migrate in connective tissue.",
    "answer": False,
    "explanation": "Fibroblasts are capable of migrating within connective tissue, especially during repair processes.",
    "ai_explanation": "Their mobility allows them to respond to injury by migrating to wound sites and producing matrix components.",
    "references": {
      "Ross & Pawlina": "Chapter 5, pp. 113",
      "Junqueira’s Basic Histology": "Chapter 6, pp. 125",
      "Wheater’s Functional Histology": "Chapter 4, pp. 65"
    },
    "category": "Histology and Embryology"
  },
  {
    "question": "Mesenchymal cells are highly proliferative during embryonic development.",
    "answer": True,
    "explanation": "Mesenchymal cells divide rapidly to populate embryonic tissues and provide progenitors for various cell types.",
    "ai_explanation": "Their proliferation supports formation of connective tissues, cartilage, bone, and muscle.",
    "references": {
      "Ross & Pawlina": "Chapter 5, pp. 109",
      "Junqueira’s Basic Histology": "Chapter 6, pp. 121",
      "Wheater’s Functional Histology": "Chapter 4, pp. 61"
    },
    "category": "Histology and Embryology"
  },
  {
    "question": "Elastic fibers are more abundant than collagen fibers in connective tissue.",
    "answer": False,
    "explanation": "Collagen fibers are usually more abundant than elastic fibers in most connective tissues.",
    "ai_explanation": "While elastic fibers provide elasticity, collagen fibers primarily provide tensile strength and bulk.",
    "references": {
      "Ross & Pawlina": "Chapter 5, pp. 113",
      "Junqueira’s Basic Histology": "Chapter 6, pp. 124",
      "Wheater’s Functional Histology": "Chapter 4, pp. 64"
    },
    "category": "Histology and Embryology"
  },
  {
    "question": "Ground substance consists mainly of proteoglycans and glycosaminoglycans.",
    "answer": True,
    "explanation": "Ground substance is rich in proteoglycans and glycosaminoglycans that trap water and provide a hydrated matrix.",
    "ai_explanation": "This hydrated gel supports diffusion of nutrients and cells within connective tissue.",
    "references": {
      "Ross & Pawlina": "Chapter 5, pp. 110",
      "Junqueira’s Basic Histology": "Chapter 6, pp. 126",
      "Wheater’s Functional Histology": "Chapter 4, pp. 63"
    },
    "category": "Histology and Embryology"
  },
  {
    "question": "Macrophages are involved in antigen presentation to T cells.",
    "answer": True,
    "explanation": "Macrophages process and present antigens to T lymphocytes to initiate immune responses.",
    "ai_explanation": "This function links innate and adaptive immunity by activating T cells.",
    "references": {
      "Ross & Pawlina": "Chapter 5, pp. 115",
      "Junqueira’s Basic Histology": "Chapter 6, pp. 128",
      "Wheater’s Functional Histology": "Chapter 4, pp. 66"
    },
    "category": "Histology and Embryology"
  },
  {
    "question": "Fibroblasts are derived from hematopoietic stem cells.",
    "answer": False,
    "explanation": "Fibroblasts originate from mesenchymal stem cells, not hematopoietic stem cells.",
    "ai_explanation": "Mesenchymal stem cells give rise to connective tissue cells, whereas hematopoietic stem cells form blood cells.",
    "references": {
      "Ross & Pawlina": "Chapter 5, pp. 109",
      "Junqueira’s Basic Histology": "Chapter 6, pp. 121",
      "Wheater’s Functional Histology": "Chapter 4, pp. 61"
    },
    "category": "Histology and Embryology"
  },
  {
    "question": "Adipose tissue plays a role in hormone production.",
    "answer": True,
    "explanation": "Adipose tissue secretes hormones such as leptin that regulate appetite and metabolism.",
    "ai_explanation": "It acts as an endocrine organ influencing energy balance and metabolic processes.",
    "references": {
      "Ross & Pawlina": "Chapter 5, pp. 131",
      "Junqueira’s Basic Histology": "Chapter 6, pp. 132",
      "Wheater’s Functional Histology": "Chapter 4, pp. 67"
    },
    "category": "Histology and Embryology"
  },
  {
    "question": "Reticular fibers are visible with routine H&E staining.",
    "answer": False,
    "explanation": "Reticular fibers require special stains like silver impregnation to be visualized.",
    "ai_explanation": "Their fine structure is not easily distinguished with standard hematoxylin and eosin stains.",
    "references": {
      "Ross & Pawlina": "Chapter 5, pp. 114",
      "Junqueira’s Basic Histology": "Chapter 6, pp. 125",
      "Wheater’s Functional Histology": "Chapter 4, pp. 64"
    },
    "category": "Histology and Embryology"
  },
  {
    "question": "Mesenchymal cells have a high nuclear to cytoplasmic ratio.",
    "answer": True,
    "explanation": "Mesenchymal cells show a relatively large nucleus compared to their scant cytoplasm.",
    "ai_explanation": "This reflects their active transcriptional state and immature phenotype.",
    "references": {
      "Ross & Pawlina": "Chapter 5, pp. 109",
      "Junqueira’s Basic Histology": "Chapter 6, pp. 121",
      "Wheater’s Functional Histology": "Chapter 4, pp. 61"
    },
    "category": "Histology and Embryology"
  },
  {
    "question": "Collagen fibers are resistant to enzymatic degradation.",
    "answer": True,
    "explanation": "Collagen fibers have strong cross-linking that makes them durable and resistant to most enzymes.",
    "ai_explanation": "This resistance ensures connective tissue maintains structural integrity under stress.",
    "references": {
      "Ross & Pawlina": "Chapter 5, pp. 112",
      "Junqueira’s Basic Histology": "Chapter 6, pp. 124",
      "Wheater’s Functional Histology": "Chapter 4, pp. 64"
    },
    "category": "Histology and Embryology"
  },
  {
    "question": "Fibroblasts can be activated by growth factors during tissue injury.",
    "answer": True,
    "explanation": "Growth factors like TGF-beta stimulate fibroblast proliferation and matrix production in wound healing.",
    "ai_explanation": "Activation enhances their capacity to restore extracellular matrix and repair tissues.",
    "references": {
      "Ross & Pawlina": "Chapter 5, pp. 113",
      "Junqueira’s Basic Histology": "Chapter 6, pp. 125",
      "Wheater’s Functional Histology": "Chapter 4, pp. 65"
    },
    "category": "Histology and Embryology"
  },
  {
    "question": "Mast cells are derived from monocytes in circulation.",
    "answer": False,
    "explanation": "Mast cells develop from distinct hematopoietic precursors different from monocytes.",
    "ai_explanation": "Though both arise from bone marrow, mast cells mature in tissues independently of monocyte lineage.",
    "references": {
      "Ross & Pawlina": "Chapter 5, pp. 116",
      "Junqueira’s Basic Histology": "Chapter 6, pp. 127",
      "Wheater’s Functional Histology": "Chapter 4, pp. 67"
    },
    "category": "Histology and Embryology"
  },
  {
    "question": "Mesenchyme forms the embryonic connective tissue.",
    "answer": True,
    "explanation": "Mesenchyme is the primitive connective tissue present during embryonic development.",
    "ai_explanation": "It is the precursor of all connective tissues and supports organogenesis.",
    "references": {
      "Ross & Pawlina": "Chapter 5, pp. 106",
      "Junqueira’s Basic Histology": "Chapter 6, pp. 120",
      "Wheater’s Functional Histology": "Chapter 4, pp. 61"
    },
    "category": "Histology and Embryology"
  },
  {
    "question": "Collagen fibers are synthesized intracellularly and secreted as procollagen.",
    "answer": True,
    "explanation": "Fibroblasts produce procollagen molecules inside the cell, which are then secreted and assembled extracellularly.",
    "ai_explanation": "Procollagen processing outside the cell forms mature collagen fibrils.",
    "references": {
      "Ross & Pawlina": "Chapter 5, pp. 112",
      "Junqueira’s Basic Histology": "Chapter 6, pp. 124",
      "Wheater’s Functional Histology": "Chapter 4, pp. 64"
    },
    "category": "Histology and Embryology"
  },

  {
    "question": "Microvilli increase the surface area of epithelial cells to enhance absorption.",
    "answer": True,
    "explanation": "Microvilli are finger-like projections that amplify the apical surface for nutrient absorption.",
    "ai_explanation": "Found abundantly on intestinal and renal tubular epithelial cells, microvilli contain a core of actin filaments that provide structural support. Their dense packing forms the brush border, critical for efficient absorption of nutrients and ions.",
    "references": {
      "Junqueira’s Basic Histology": "Chapter 4, pp. 74-75",
      "Ross & Pawlina": "Chapter 2, pp. 44"
    },
    "category": "Histology and Embryology"
  },
  {
    "question": "Simple squamous epithelium facilitates rapid diffusion of gases and fluids.",
    "answer": True,
    "explanation": "Simple squamous cells are thin and flat, allowing efficient exchange across the epithelium.",
    "ai_explanation": "This epithelium lines blood vessels (endothelium), body cavities (mesothelium), and alveoli, where thinness permits rapid gas exchange and filtration. Damage to these cells can impair organ function, such as in pulmonary edema.",
    "references": {
      "Ross & Pawlina": "Chapter 17, pp. 629-630",
      "Wheater’s Functional Histology": "Chapter 14, pp. 278-279"
    },
    "category": "Histology and Embryology"
  },
  {
    "question": "Tight junctions form a seal between epithelial cells to prevent paracellular leakage.",
    "answer": True,
    "explanation": "Tight junctions create a barrier that controls passage of substances between cells.",
    "ai_explanation": "Located near the apical surface, tight junctions consist of claudins and occludins that regulate selective permeability, maintaining distinct compartments and protecting underlying tissues from pathogens or toxins.",
    "references": {
      "Junqueira’s Basic Histology": "Chapter 4, pp. 77",
      "Ross & Pawlina": "Chapter 2, pp. 45"
    },
    "category": "Histology and Embryology"
  },
  {
    "question": "Pseudostratified columnar epithelium appears multilayered but all cells contact the basement membrane.",
    "answer": True,
    "explanation": "Pseudostratified epithelium has nuclei at different levels, giving a layered appearance though all cells rest on the basal lamina.",
    "ai_explanation": "This epithelium lines much of the respiratory tract, where ciliated cells and goblet cells work together to trap and clear inhaled particles, playing a vital role in pulmonary defense.",
    "references": {
      "Ross & Pawlina": "Chapter 17, pp. 631",
      "Wheater’s Functional Histology": "Chapter 4, pp. 67"
    },
    "category": "Histology and Embryology"
  },
  {
    "question": "The basement membrane consists of basal lamina and reticular lamina.",
    "answer": True,
    "explanation": "The basement membrane supports epithelial cells and separates them from connective tissue.",
    "ai_explanation": "The basal lamina is secreted by epithelial cells, composed mainly of collagen IV and laminin, while the reticular lamina, produced by connective tissue fibroblasts, contains collagen III. Together, they provide mechanical support and regulate cell behavior.",
    "references": {
      "Wheater’s Functional Histology": "Chapter 2, pp. 53",
      "Junqueira’s Basic Histology": "Chapter 4, pp. 79"
    },
    "category": "Histology and Embryology"
  },
  {
    "question": "The notochord induces formation of the neural plate during embryogenesis.",
    "answer": True,
    "explanation": "The notochord is a rod-like structure that signals overlying ectoderm to become neuroectoderm.",
    "ai_explanation": "Through secretion of signaling molecules such as Sonic Hedgehog (SHH), the notochord directs the ectoderm to thicken into the neural plate, the precursor of the central nervous system. Defects in this process can cause neural tube defects.",
    "references": {
      "Langman’s Medical Embryology": "Chapter 7, pp. 102-103",
      "Moore, Persaud, Torchia": "Chapter 10, pp. 135"
    },
    "category": "Histology and Embryology"
  },
  {
    "question": "Keratinized stratified squamous epithelium provides a tough, water-resistant surface.",
    "answer": True,
    "explanation": "Keratinized epithelium contains layers of dead cells filled with keratin protein.",
    "ai_explanation": "This epithelium is found in the skin epidermis and protects underlying tissues from abrasion, dehydration, and microbial invasion. The keratin forms a durable, insoluble barrier essential for survival in terrestrial environments.",
    "references": {
      "Ross & Pawlina": "Chapter 17, pp. 635",
      "Wheater’s Functional Histology": "Chapter 4, pp. 70"
    },
    "category": "Histology and Embryology"
  },
  {
    "question": "Embryonic mesenchyme gives rise primarily to connective tissues.",
    "answer": True,
    "explanation": "Mesenchyme is loosely organized embryonic connective tissue.",
    "ai_explanation": "Derived mainly from mesoderm, mesenchyme cells differentiate into fibroblasts, chondroblasts, osteoblasts, and other connective tissue types, contributing to the formation of skeletal structures, blood vessels, and dermis.",
    "references": {
      "Langman’s Medical Embryology": "Chapter 8, pp. 110",
      "Before We Are Born": "Chapter 8, pp. 122"
    },
    "category": "Histology and Embryology"
  },
  {
    "question": "Endocrine glands secrete hormones directly into the bloodstream.",
    "answer": True,
    "explanation": "Endocrine glands lack ducts and release secretions into extracellular fluid and blood.",
    "ai_explanation": "Hormones produced by endocrine glands regulate metabolism, growth, and homeostasis. Unlike exocrine glands, they target distant organs and maintain systemic physiological balance.",
    "references": {
      "Junqueira’s Basic Histology": "Chapter 12, pp. 215",
      "Ross & Pawlina": "Chapter 12, pp. 460"
    },
    "category": "Histology and Embryology"
  },
  {
    "question": "Epithelial cells display polarity with distinct apical, lateral, and basal domains.",
    "answer": True,
    "explanation": "Cell polarity allows directional functions such as absorption and secretion.",
    "ai_explanation": "Polarity is essential for epithelial function, with the apical surface often specialized for absorption or secretion, lateral surfaces for cell junctions, and basal surface anchored to the basement membrane. Loss of polarity is implicated in cancer progression.",
    "references": {
      "Ross & Pawlina": "Chapter 2, pp. 40-41",
      "Junqueira’s Basic Histology": "Chapter 4, pp. 73"
    },
    "category": "Histology and Embryology"
  }

]


    add_batch_questions(questions)