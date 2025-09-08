# Getting Started with Ge-ez (ግእዝ)

Welcome to Ge-ez, the world's first complete Amharic programming language! This guide will help you get started with writing your first programs in Amharic.

## 🚀 Installation

### Option 1: Install from Source
```bash
git clone https://github.com/Mightyshambel/Ge-ez.git
cd Ge-ez
pip install -r requirements.txt
```

### Option 2: Install via pip (Coming Soon)
```bash
pip install geez-lang
```

## 🎯 Your First Program

Create a file called `hello.geez`:

```amharic
ማተም "ሰላም ዓለም!"
```

Run it:
```bash
python3 main.py hello.geez
```

Output:
```
ሰላም ዓለም!
```

## 📝 Basic Syntax

### Variables
```amharic
አስተዋውቅ ስም = "አሊ"
አስተዋውቅ አድሜ = 25
አስተዋውቅ አውታረመረብ = እውነት
```

### Control Flow
```amharic
ከሆነ አድሜ > 18 {
    ማተም "አዋቂ"
} አለበለዚያ {
    ማተም "ልጅ"
}
```

### Loops
```amharic
አስተዋውቅ ቁጥር = 1
ሳለ ቁጥር <= 5 {
    ማተም ቁጥር
    ቁጥር = ቁጥር + 1
}
```

### Functions
```amharic
ዘዴ ማተም_ስም(ስም) {
    ማተም "ስም:", ስም
}

ማተም_ስም("አሊ")
```

## 🏗️ Object-Oriented Programming

### Classes
```amharic
ክፍል ሰው {
    ዘዴ መጀመሪያ(ራሱ, ስም, አድሜ) {
        ራሱ.ስም = ስም
        ራሱ.አድሜ = አድሜ
    }
    
    ዘዴ ማተም_መረጃ(ራሱ) {
        ማተም "ስም:", ራሱ.ስም
        ማተም "አድሜ:", ራሱ.አድሜ
    }
}

አስተዋውቅ ሰው_1 = አዲስ ሰው("አሊ", 25)
ሰው_1.ማተም_መረጃ()
```

## 📁 File Operations

```amharic
# Write to file
ጻፍ "test.txt" "Hello World"

# Read from file
አስተዋውቅ ይዘት = አንብብ "test.txt"
ማተም ይዘት

# Check if file exists
ከሆነ አለ "test.txt" {
    ማተም "ፋይል አለ"
}
```

## 🛡️ Error Handling

```amharic
ሞክር {
    አስተዋውቅ ቁጥር = 10 / 0
} ያዝ ስህተት {
    ማተም "ስህተት ተፈጥሯል:", ስህተት
} በመጨረሻ {
    ማተም "አልተለወጠም"
}
```

## 📚 Data Structures

### Lists
```amharic
አስተዋውቅ ዝርዝር = [1, 2, 3, 4, 5]
ማተም ዝርዝር[0]  # Output: 1
```

### Dictionaries
```amharic
አስተዋውቅ ንብብ = {"ስም": "አሊ", "አድሜ": 25}
ማተም ንብብ["ስም"]  # Output: አሊ
```

## 🔧 Built-in Functions

```amharic
# Type checking
ማተም ዓይነት("ሰላም")  # Output: string

# String operations
አስተዋውቅ ስም = "አሊ"
ማተም ርዝመት(ስም)  # Output: 2

# Math functions
ማተም ከፍተኛ(1, 2, 3)  # Output: 3
ማተም ዠቅተኛ(1, 2, 3)  # Output: 1
```

## 🎨 Examples

Check out the `examples/` directory for more comprehensive examples:
- `hello_world.geez` - Basic hello world
- `variables.geez` - Variable examples
- `functions.geez` - Function examples
- `classes.geez` - Class examples
- `file_operations.geez` - File I/O examples

## 🆘 Getting Help

- Check the [Language Reference](language-reference.md) for complete syntax
- Look at [Examples](examples/) for code samples
- Read [API Documentation](api.md) for detailed function reference
- Report issues on [GitHub](https://github.com/Mightyshambel/Ge-ez/issues)

## 🎉 Next Steps

1. Try the examples in the `examples/` directory
2. Read the [Language Reference](language-reference.md)
3. Build your own Amharic programs
4. Contribute to the project!

Welcome to the world of Amharic programming! 🇪🇹
