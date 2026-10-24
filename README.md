# synthetic-correlation-lab

## Français

Générer des marges discrètes couplées par une copule gaussienne.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m synthetic_correlation_lab examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Échantillonne une copule gaussienne bivariée et applique les quantiles de deux marges discrètes fournies. Les comptes réalisés exposent l’écart entre probabilités déclarées et petit échantillon.

### Limites

Corrélation latente, pas corrélation de Pearson des catégories ; marges finies non exactes, sans apprentissage de données privées ni confidentialité différentielle.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Generate discrete marginals coupled by a Gaussian copula.

Synthetic data; no network access or secret required.

```sh
python -m synthetic_correlation_lab examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Samples a bivariate Gaussian copula and applies quantiles of two supplied discrete margins. Realized counts expose the gap between declared probabilities and a finite sample.

### Limits

Latent correlation, not Pearson correlation of categories; finite margins are not exact, no private-data learning or differential privacy.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Generar marginales discretas acopladas por una cópula gaussiana.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m synthetic_correlation_lab examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Muestrea una cópula gaussiana bivariada y aplica cuantiles de dos marginales discretas. Los conteos muestran diferencia entre probabilidades y muestra finita.

### Límites

Correlación latente, no Pearson de categorías; marginales finitas no exactas, sin aprendizaje de datos privados o privacidad diferencial.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.multivariate_normal.html
