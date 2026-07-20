class WidgetRegistry {

    constructor() {

        this.widgets = new Map();

    }

    register(widget) {

        if (!widget?.id) {

            throw new Error(
                "Widget id required.",
            );

        }

        this.widgets.set(
            widget.id,
            widget,
        );

    }

    unregister(id) {

        this.widgets.delete(id);

    }

    get(id) {

        return this.widgets.get(id);

    }

    getAll() {

        return [...this.widgets.values()]
            .sort(
                (a, b) =>
                    (a.order ?? 999) -
                    (b.order ?? 999),
            );

    }

    has(id) {

        return this.widgets.has(id);

    }

    clear() {

        this.widgets.clear();

    }

}

export default new WidgetRegistry();