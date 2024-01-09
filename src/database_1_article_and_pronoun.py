# df = pd.DataFrame(data, columns=['単語', '格変化', '例文', '例文の日本語訳'])


data = [
    ['der', 'Nominative', 'Der Hund ist groß.', '犬は大きいです。'],
    ['der', 'Genitive', 'Das ist das Auto der Lehrerin.', 'これは先生の車です。'],
    ['der', 'Dative', 'Ich gebe das Buch der Freundin.', '私は友達にその本を渡します。'],
    ['der', 'Accusative', 'Ich sehe den Mann.', '私はその男性を見ています。']
] + [
    ['die', 'Nominative', 'Die Blumen sind schön.', '花は美しいです。'],
    ['die', 'Genitive', 'Das ist das Haus der Familie.', 'これは家族の家です。'],
    ['die', 'Dative', 'Ich gebe die Schokolade der Freundin.', '私は友達にそのチョコレートを渡します。'],
    ['die', 'Accusative', 'Ich sehe die Katze.', '私はその猫を見ています。']
] + [
    ['das', 'Nominative', 'Das Buch ist interessant.', 'その本は面白いです。'],
    ['das', 'Genitive', 'Das ist das Auto des Mannes.', 'これはその男性の車です。'],
    ['das', 'Dative', 'Ich gebe das Geld dem Kind.', '私はそのお金を子供に渡します。'],
    ['das', 'Accusative', 'Ich sehe das Mädchen.', '私はその少女を見ています。']
] + [
    ['die', 'Nominative', 'Die Kinder spielen im Garten.', '子供たちは庭で遊んでいます。'],
    ['der', 'Genitive', 'Das sind die Spielzeuge der Kinder.', 'これは子供たちのおもちゃです。'],
    ['den', 'Dative', 'Ich gebe den Kindern Süßigkeiten.', '私は子供たちにお菓子をあげます。'],
    ['die', 'Accusative', 'Ich sehe die Kinder.', '私は子供たちを見ています。']
] + [
    ['ein', 'Nominative', 'Ein Mann geht spazieren.', '男性が散歩しています。'],
    ['eines', 'Genitive', 'Das ist das Buch eines Freundes.', 'これは友達の本です。'],
    ['einem', 'Dative', 'Ich gebe einem Mann einen Apfel.', '私は男性にりんごをあげます。'],
    ['einen', 'Accusative', 'Ich sehe einen Mann.', '私は男性を見ています。']
] + [
    ['eine', 'Nominative', 'Eine Frau liest ein Buch.', '女性が本を読んでいます。'],
    ['einer', 'Genitive', 'Das ist die Tasche einer Freundin.', 'これは友達のバッグです。'],
    ['einer', 'Dative', 'Ich gebe einer Frau Blumen.', '私は女性に花をあげます。'],
    ['eine', 'Accusative', 'Ich sehe eine Frau.', '私は女性を見ています。']
] + [
    ['ein', 'Nominative', 'Ein Kind spielt im Park.', '中性の子供が公園で遊んでいます。'],
    ['eines', 'Genitive', 'Das ist das Spielzeug eines Kindes.', 'これは子供のおもちゃです。'],
    ['einem', 'Dative', 'Ich gebe einem Kind einen Ball.', '私は子供にボールをあげます。'],
    ['ein', 'Accusative', 'Ich sehe ein Kind.', '私は子供を見ています。']
] + [
    ['keine', 'Nominative', 'Es gibt keine Bücher auf dem Tisch.', 'テーブルの上に本はありません。'],
    ['keiner', 'Genitive', 'Das sind die Taschen keiner Studenten.', 'これは学生たちのかばんではありません。'],
    ['keinen', 'Dative', 'Ich gebe keinen Kindern Süßigkeiten.', '私は子供たちにお菓子をあげません。'],
    ['keine', 'Accusative', 'Ich sehe keine Blumen im Garten.', '庭には花はありません。']
] + [
    ['dieser', 'Nominative', 'Dieser Hund ist groß.', 'この犬は大きいです。'],
    ['dieses', 'Genitive', 'Das ist das Spielzeug dieses Kindes.', 'これはこの子供のおもちゃです。'],
    ['diesem', 'Dative', 'Ich gebe diesem Kind einen Ball.', '私はこの子供にボールをあげます。'],
    ['diesen', 'Accusative', 'Ich sehe diesen Hund.', '私はこの犬を見ています。']
] + [
    ['jene', 'Nominative', 'Jene Frau ist freundlich.', 'あの女性は親切です。'],
    ['jener', 'Genitive', 'Das ist das Buch jener Freundin.', 'これはあの友達の本です。'],
    ['jener', 'Dative', 'Ich gebe jener Frau ein Geschenk.', '私はあの女性にプレゼントをあげます。'],
    ['jene', 'Accusative', 'Ich sehe jene Frau.', '私はあの女性を見ています。']
] + [
    ['solche', 'Nominative', 'Solche Bücher sind interessant.', 'そのような本は面白いです。'],
    ['solcher', 'Genitive', 'Das sind die Taschen solcher Studenten.', 'これはそのような学生たちのかばんです。'],
    ['solchen', 'Dative', 'Ich gebe solchen Kindern Süßigkeiten.', '私はそのような子供たちにお菓子をあげます。'],
    ['solche', 'Accusative', 'Ich sehe solche Blumen im Garten.', '私は庭にそのような花を見ています。']
] + [
    ['jedes', 'Nominative', 'Jedes Kind spielt gerne.', 'どの子供も喜んで遊びます。'],
    ['jedes', 'Genitive', 'Das ist das Spielzeug jedes Kindes.', 'これはどの子供のおもちゃです。'],
    ['jedem', 'Dative', 'Ich gebe jedem Kind einen Ball.', '私はどの子供にボールをあげます。'],
    ['jedes', 'Accusative', 'Ich sehe jedes Kind.', '私はどの子供も見ています。']
]

