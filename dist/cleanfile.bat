echo on
set chaine=COUVERTURE_

for %%1 in ("*.epub") do (
SANITYFILE.exe %%1
)