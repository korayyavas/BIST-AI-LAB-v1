export type WidgetFactory<T = unknown> = () => T;

export interface WidgetDefinition<T = unknown> {
  id: string;
  title: string;
  description?: string;
  order?: number;
  enabled?: boolean;
  factory: WidgetFactory<T>;
}

class WidgetRegistry {
  private registry = new Map<string, WidgetDefinition>();

  register(definition: WidgetDefinition): void {
    if (this.registry.has(definition.id)) {
      console.warn(
        `[Dashboard] Widget '${definition.id}' is already registered.`,
      );
      return;
    }

    this.registry.set(definition.id, definition);
  }

  unregister(id: string): void {
    this.registry.delete(id);
  }

  get<T = unknown>(
    id: string,
  ): WidgetDefinition<T> | undefined {
    return this.registry.get(id) as
      | WidgetDefinition<T>
      | undefined;
  }

  has(id: string): boolean {
    return this.registry.has(id);
  }

  clear(): void {
    this.registry.clear();
  }

  getAll(): WidgetDefinition[] {
    return [...this.registry.values()].sort(
      (a, b) => (a.order ?? 999) - (b.order ?? 999),
    );
  }

  getEnabled(): WidgetDefinition[] {
    return this.getAll().filter(
      (widget) => widget.enabled !== false,
    );
  }

  size(): number {
    return this.registry.size;
  }
}

export const widgetRegistry = new WidgetRegistry();

export default widgetRegistry;