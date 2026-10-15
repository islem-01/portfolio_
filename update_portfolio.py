from pathlib import Path
root=Path('/mnt/data/portfolio_edit')
# Home profile wording and remove IIT identity subtitle line (keep the degree details in the profile)
p=root/'index.html'; s=p.read_text()
s=s.replace('Étudiante ingénieure en Génie Logiciel<br>et Informatique Décisionnelle','Étudiante en 5e année du cycle ingénieur<br>en Génie Logiciel et Informatique Distribuée')
s=s.replace('<p class="muted">Institut International de Technologie de Sfax (IIT)</p>','<p class="muted">Institut International de Technologie de Sfax</p>')
s=s.replace('Je conçois des applications web et mobiles en associant développement logiciel, gestion des données et fonctionnalités d’intelligence artificielle. J’aime transformer des besoins concrets en solutions accessibles, cohérentes et utiles.','À la recherche d’un stage de fin d’études, je m’intéresse particulièrement au développement Full-Stack, à l’IA générative et aux pratiques DevOps (CI/CD, GitLab CI).')
p.write_text(s)
# Parcours: remove logo IIT, update degree title and preserve Communication & design section here
p=root/'parcours.html'; s=p.read_text()
s=s.replace('Cycle ingénieur — Génie Logiciel et Informatique Décisionnelle','Cycle ingénieur — Génie Logiciel et Informatique Distribuée')
s=s.replace('<img src="assets/logo-IIT.png" alt="Logo de l\'Institut International de Technologie" style="width:min(210px,100%);background:#fff;border-radius:8px;padding:8px;margin-top:10px">','')
p.write_text(s)
# Competences: remove the Communication & design skill card only
p=root/'competences.html'; s=p.read_text()
start=s.find('<article class="skill-card"><h3>Communication &amp; design</h3>')
if start!=-1:
    end=s.find('</article>',start)+len('</article>')
    s=s[:start]+s[end:]
p.write_text(s)
# Contact: remove standalone CV download contact row (header CV button remains site-wide)
p=root/'contact.html'; s=p.read_text()
needle='<a class="contact-link" href="assets/Islem_Zouari_CV_PFE2027.tex.pdf" download><span class="stat-icon">⇩</span><span><strong>Curriculum vitæ</strong><br>Télécharger le CV en PDF</span></a>'
s=s.replace(needle,'')
p.write_text(s)
# Projects: add academic/personal/professional filters, clickable cards, and richer project summaries
p=root/'projets.html'; s=p.read_text()
s=s.replace('Explorez une sélection de projets académiques et professionnels. Les visuels de démonstration sont créés en CSS lorsque aucune capture de l’application n’a été fournie ; les médias réels disponibles sont intégrés dans les pages de détail.','Explorez mes réalisations avec des filtres par type de projet. Sélectionnez une carte pour ouvrir sa fiche détaillée, consulter les fonctionnalités et découvrir les médias disponibles.')
old='<div class="filters" role="group" aria-label="Filtrer les projets"><button class="filter-btn" data-filter="all" aria-pressed="true">Tous</button><button class="filter-btn" data-filter="mobile" aria-pressed="false">Développement mobile</button><button class="filter-btn" data-filter="web" aria-pressed="false">Web / Full Stack</button><button class="filter-btn" data-filter="ai" aria-pressed="false">Intelligence artificielle</button><button class="filter-btn" data-filter="vision" aria-pressed="false">Computer Vision</button><button class="filter-btn" data-filter="genai" aria-pressed="false">IA générative</button></div>'
new='<div class="filters" role="group" aria-label="Filtrer les projets"><button class="filter-btn" data-filter="all" aria-pressed="true">Tous les projets</button><button class="filter-btn" data-filter="academic" aria-pressed="false">Projets académiques</button><button class="filter-btn" data-filter="personal" aria-pressed="false">Projets personnels</button><button class="filter-btn" data-filter="professional" aria-pressed="false">Projets professionnels</button></div>'
s=s.replace(old,new)
# Assign project types to all cards while retaining technology categories as secondary classes
repls={
'<article class="project-card" data-category="ai genai">':'<article class="project-card project-card-clickable" data-category="academic" data-card-href="projets/smartcampus-ai.html" tabindex="0" role="link" aria-label="Ouvrir le projet SmartCampus AI">',
'<article class="project-card" data-category="ai vision">':'<article class="project-card project-card-clickable" data-category="academic" data-card-href="projets/smart-exam.html" tabindex="0" role="link" aria-label="Ouvrir le projet Smart Exam Monitoring System">',
'<article class="project-card" data-category="web ai">':'<article class="project-card project-card-clickable" data-category="professional" data-card-href="projets/smartevent360.html" tabindex="0" role="link" aria-label="Ouvrir le projet SmartEvent360">',
'<article class="project-card" data-category="mobile">':'<article class="project-card project-card-clickable" data-category="professional" data-card-href="projets/chrono-sport.html" tabindex="0" role="link" aria-label="Ouvrir le projet Chrono Sport">',
'<article class="project-card" data-category="mobile web">':'<article class="project-card project-card-clickable" data-category="professional" data-card-href="projets/gestion-scolaire.html" tabindex="0" role="link" aria-label="Ouvrir le projet de gestion scolaire">',
'<article class="project-card"><div class="project-visual visual-ai">':'<article class="project-card project-card-clickable" data-category="personal" data-card-href="projets/rappel-medicaments.html" tabindex="0" role="link" aria-label="Ouvrir le projet Rappel de médicaments"><div class="project-visual visual-ai">',
'<article class="project-card" data-category="web"><div class="project-visual visual-event">':'<article class="project-card project-card-clickable" data-category="professional" data-card-href="projets/wordpress-evenements.html" tabindex="0" role="link" aria-label="Ouvrir la plateforme de gestion d’événements"><div class="project-visual visual-event">',
'<article class="project-card" data-category="web"><div class="project-visual"><span class="visual-icon">▣</span><span class="visual-label">WEB · ACADÉMIQUE</span>':'<article class="project-card project-card-clickable" data-category="personal" data-card-href="projets/bibliotheque.html" tabindex="0" role="link" aria-label="Ouvrir le projet Bibliothèque"><div class="project-visual"><span class="visual-icon">▣</span><span class="visual-label">WEB · ANGULAR</span>',
'<article class="project-card" data-category="web"><div class="project-visual"><span class="visual-icon">✚</span>':'<article class="project-card project-card-clickable" data-category="personal" data-card-href="projets/pharmacy.html" tabindex="0" role="link" aria-label="Ouvrir le projet Pharmacy Management System"><div class="project-visual"><span class="visual-icon">✚</span>',
'<article class="project-card" data-category="web"><div class="project-visual"><span class="visual-icon">▤</span><span class="visual-label">BADGE SCANNER</span>':'<article class="project-card project-card-clickable" data-category="personal" data-card-href="projets/badge-scanner.html" tabindex="0" role="link" aria-label="Ouvrir le projet Smart Badge Scanner"><div class="project-visual"><span class="visual-icon">▤</span><span class="visual-label">BADGE SCANNER</span>'
}
for a,b in repls.items(): s=s.replace(a,b)
s=s.replace('<h3>SmartCampus AI</h3>','<h3>SmartCampus AI</h3>')
s=s.replace('<p>Projet référencé dans les ressources du portfolio ; détails à compléter depuis son README ou son dépôt.</p><div class="tags"><span>Projet académique</span></div>','<p>Application de gestion de bibliothèque avec catalogue de livres, emprunts, espaces ADMIN/USER, statistiques et authentification Firebase.</p><div class="tags"><span>Angular 20</span><span>Spring Boot</span><span>Firebase Auth</span><span>Chart.js</span></div>')
s=s.replace('<h3>Pharmacy</h3><p>Projet présent dans les ressources fournies ; contenu technique à confirmer.</p><div class="tags"><span>Projet académique</span></div>','<h3>Pharmacy Management System</h3><p>Application full-stack pour gérer patients, médicaments, ordonnances, stocks et alertes, avec authentification par rôles.</p><div class="tags"><span>Angular 20</span><span>ASP.NET Core</span><span>SQL Server</span><span>JWT</span></div>')
s=s.replace('<h3>Badge Scanner</h3><p>Projet référencé dans le dossier média ; description et technologies à confirmer.</p><div class="tags"><span>Projet académique</span></div>','<h3>Smart Badge Scanner</h3><p>Application mobile de pointage par QR code, avec suivi des présences, espaces administrateur et employé et génération de rapports PDF.</p><div class="tags"><span>Flutter</span><span>Firebase</span><span>Google ML Kit</span></div>')
p.write_text(s)
# Make experience cards explicitly chronological descending (existing order is correct) and standardize date notation
p=root/'experiences.html'; s=p.read_text()
s=s.replace('Octobre — Décembre 2026 · période à confirmer','Octobre – Décembre 2026 · période à confirmer')
s=s.replace('Mars — Juin 2026','Mars – Juin 2026')
p.write_text(s)
# CSS: brighten paragraph text, increase readable text size, improve clickable cards and filter transition
p=root/'assets/main.css'; s=p.read_text()
s += '''\n/* Lisibilité renforcée : paragraphes plus clairs et légèrement plus grands */\n.page-head p,.hero-copy>p:not(.muted),.timeline-card p,.panel p,.panel li,.skill-card p,.muted{color:#e1e9f7;font-size:15px;line-height:1.75}\n.project-body p{color:#d5e0f3;font-size:13px;line-height:1.7}\n.timeline-card .date{font-size:12px}\n.project-card-clickable{cursor:pointer;position:relative;transition:transform .25s ease,border-color .25s ease,box-shadow .25s ease}\n.project-card-clickable:hover,.project-card-clickable:focus-visible{transform:translateY(-6px);border-color:#56c8ff;box-shadow:0 18px 42px rgba(35,112,255,.2)}\n.project-card-clickable:after{content:'Ouvrir le projet ↗';position:absolute;right:13px;top:10px;font-size:10px;color:#dff6ff;background:rgba(7,18,39,.78);border:1px solid rgba(86,200,255,.38);border-radius:20px;padding:4px 8px;opacity:0;transform:translateY(-3px);transition:opacity .2s,transform .2s;z-index:3}\n.project-card-clickable:hover:after,.project-card-clickable:focus-visible:after{opacity:1;transform:translateY(0)}\nbody.light-mode .page-head p,body.light-mode .hero-copy>p:not(.muted),body.light-mode .timeline-card p,body.light-mode .panel p,body.light-mode .panel li,body.light-mode .skill-card p,body.light-mode .muted{color:#344762}\nbody.light-mode .project-body p{color:#405571}\n@media(max-width:640px){.page-head p,.hero-copy>p:not(.muted),.timeline-card p,.panel p,.panel li,.skill-card p,.muted{font-size:14px}}\n'''
p.write_text(s)
