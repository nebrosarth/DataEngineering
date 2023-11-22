# DataEngineering

Данное приложение позволяет генерировать пропущенные слова в предложении,
используя обученную нейросеть `bert-base-uncased`.

## Пример использования

```
maskFiller = MaskFiller()  # Создание экземпляра класса MaskFiller
maskFiller.fill_mask("Would you like to drink [MASK] with me?")  # Заполнение маски
```

## Пример вывода

```
Variant #0, word=this: would you like to drink this with me?
Variant #1, word=it: would you like to drink it with me?
Variant #2, word=water: would you like to drink water with me?
Variant #3, word=coffee: would you like to drink coffee with me?
Variant #4, word=tea: would you like to drink tea with me?
```