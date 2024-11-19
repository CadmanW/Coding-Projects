class Position {
    x;
    y;
    a;

    constructor(x, y) {
        this.x = x;
        this.y = y;
    }

    add(position) {
        this.x += position.x;
        this.y += position.y;
    }

    times(num) {
        this.x *= num;
        this.y *= num;
    }

    rotate(deg) {
        // https://math.sci.ccny.cuny.edu/document/Rotation+of+Axes
        this.x = (this.x * Math.cos(deg)) - (this.y * Math.sin(deg));
        this.y = (this.x * Math.sin(deg)) + (this.y * Math.cos(deg));
    }
}