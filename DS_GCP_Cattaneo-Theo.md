## Création d'un Service Account :

« Décrivez les étapes pour créer un Service Account dans GCP. Quelles sont les
bonnes pratiques à suivre en matière de gestion des clés et de sécurité ? »

> Pour créer un Service Account dans GCP, on va dans "IAM et administration" puis dans "Comptes de service" et on clique sur "+ CRÉER UN COMPTE DE SERVICE", puis on rentre les informations necessaires. Il faut garder la clé de manière confidentielle (ne pas l'exposer dans une repo git) et limiter les accès du compte de service au strict minimum.

## Création d'un Bucket :

- « Comment créer un bucket sur Google Cloud Storage ? Précisez les configurations importantes à définir (localisation, politique de conservation, etc.) et comment celles-ci impactent la sécurité et la performance. »

> Pour créer un Bucket dans GCP, on va dans "Cloud Storage" puis dans "Bucket" et on clique sur "+ CRÉER", puis on rentre les informations necessaires. On peut choisir Multi-région pour une disponibilité maximale ou choisir deux régions en particulier avec Dual-Région. La classe de stockage dépend de la fréquence d'accès, pour une application on prend Standard. La politique de conservation et importante car elle gère la durée pour laquelle nos objets seront restaurables après suppression.


## Gestion des droits (IAM) :

- « En quoi consiste la gestion des identités et des accès (IAM) sur GCP ? Donnez un exemple concret de configuration des droits pour limiter l'accès à une ressource critique. »

> Elle consiste à donner des droits spécifiques aux utilisateurs selon ce dont ils ont besoins, par exemple, "Administrateur d'instances Compute (v1)" donne l'accès à la création de machines virtuelles/

## Configuration de la facturation :

- « Expliquez comment configurer la facturation sur GCP. Quelles précautions recommanderiez-vous pour éviter des coûts imprévus lors du déploiement de projets ? »

> La facturation est accessible dans l'onglet "Facturation", on peux analyser nos coûts sur une periode donnée. Pour eviter les couts imprevu, on peut mettre en place des alertes par mail quand on atteint un seuil de dépense définie sur une periode donnée. On peut également mettre en place un Pub/Sub.