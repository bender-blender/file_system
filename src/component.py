from abc import ABC, abstractmethod

# Абстрактный компонент
class Component(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass

# Листовой компонент
class Leaf(Component):
    def __init__(self, name: str):
        self.name = name

    def operation(self) -> str:
        return f"Leaf: {self.name}"

# Составной компонент
class Composite(Component):
    def __init__(self):
        self.children = []

    def add(self, component: Component) -> None:
        self.children.append(component)

    def remove(self, component: Component) -> None:
        self.children.remove(component)

    def operation(self) -> str:
        results = [child.operation() for child in self.children]
        return f"Composite:\n" + "\n".join(results)

# Пример использования
if __name__ == "__main__":
    # Создаем листья
    leaf1 = Leaf("Leaf 1")
    leaf2 = Leaf("Leaf 2")

    # Создаем составной объект
    composite = Composite()
    composite.add(leaf1)
    composite.add(leaf2)

    # Выводим результат операции
    print(composite.operation())
