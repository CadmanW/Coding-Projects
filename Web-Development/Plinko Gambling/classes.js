class Vector {
    x;
    y;
    a;

    constructor(x, y, a) {
        this.x = x;
        this.y = y;
        this.a = a;
    }

    add(vector) {
        this.x += vector.x;
        this.y += vector.y;
        this.a += vector.a;
    }

    rotate(deg) {
        // https://math.sci.ccny.cuny.edu/document/Rotation+of+Axes
        this.x = (this.x * Math.cos(deg)) - (this.y * Math.sin(deg));
        this.y = (this.x * Math.sin(deg)) + (this.y * Math.cos(deg));
    }
}