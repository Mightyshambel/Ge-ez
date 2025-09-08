# Ge-ez Language Reference

Complete reference for the Ge-ez (ግእዝ) Amharic programming language.

## 📝 Table of Contents

1. [Keywords](#keywords)
2. [Data Types](#data-types)
3. [Variables](#variables)
4. [Operators](#operators)
5. [Control Flow](#control-flow)
6. [Functions](#functions)
7. [Classes & Objects](#classes--objects)
8. [Error Handling](#error-handling)
9. [File Operations](#file-operations)
10. [Built-in Functions](#built-in-functions)
11. [Data Structures](#data-structures)

## 🔑 Keywords

| Amharic | English | Description |
|---------|---------|-------------|
| `አስተዋውቅ` | VAR | Variable declaration |
| `ከሆነ` | IF | Conditional statement |
| `አለበለዚያ` | ELSE | Alternative condition |
| `ሳለ` | WHILE | While loop |
| `ለ` | FOR | For loop |
| `ዘዴ` | METHOD | Method definition |
| `መለስ` | RETURN | Return value |
| `ማተም` | PRINT | Print output |
| `ግብአት` | INPUT | Get user input |
| `ሞክር` | TRY | Try block |
| `ያዝ` | CATCH | Catch block |
| `በመጨረሻ` | FINALLY | Finally block |
| `አስተላልፍ` | THROW | Throw exception |
| `ክፍል` | CLASS | Class definition |
| `አዲስ` | NEW | Object instantiation |
| `ራሱ` | SELF | Self reference |
| `የራሱ` | THIS | This reference |
| `ተወላጅ` | INHERITS | Inheritance |
| `ባህሪ` | PROPERTY | Property definition |

## 📊 Data Types

### Numbers
```amharic
አስተዋውቅ ቁጥር = 42
አስተዋውቅ አስርዮሽ = 3.14
```

### Strings
```amharic
አስተዋውቅ ስም = "አሊ"
አስተዋውቅ መልዕክት = 'ሰላም ዓለም!'
```

### Booleans
```amharic
አስተዋውቅ እውነት = እውነት
አስተዋውቅ ሐሰት = ሐሰት
```

### Lists
```amharic
አስተዋውቅ ዝርዝር = [1, 2, 3, 4, 5]
አስተዋውቅ ስሞች = ["አሊ", "ብርሃን", "ሰላም"]
```

### Dictionaries
```amharic
አስተዋውቅ ንብብ = {"ስም": "አሊ", "አድሜ": 25}
አስተዋውቅ አውታረመረብ = {"አውታረመረብ": እውነት}
```

## 🔧 Variables

### Declaration
```amharic
አስተዋውቅ ስም = "አሊ"
አስተዋውቅ አድሜ = 25
```

### Assignment
```amharic
ስም = "ብርሃን"
አድሜ = 30
```

### Multiple Assignment
```amharic
አስተዋውቅ ስም, አድሜ = "አሊ", 25
```

## ⚡ Operators

### Arithmetic
| Operator | Description | Example |
|----------|-------------|---------|
| `+` | Addition | `5 + 3` |
| `-` | Subtraction | `5 - 3` |
| `*` | Multiplication | `5 * 3` |
| `/` | Division | `5 / 3` |
| `%` | Modulus | `5 % 3` |

### Comparison
| Operator | Description | Example |
|----------|-------------|---------|
| `==` | Equal | `5 == 5` |
| `!=` | Not equal | `5 != 3` |
| `<` | Less than | `5 < 10` |
| `>` | Greater than | `5 > 3` |
| `<=` | Less than or equal | `5 <= 5` |
| `>=` | Greater than or equal | `5 >= 5` |

### Logical
| Operator | Description | Example |
|----------|-------------|---------|
| `እና` | AND | `እውነት እና ሐሰት` |
| `ወይም` | OR | `እውነት ወይም ሐሰት` |
| `አይደለም` | NOT | `አይደለም እውነት` |

## 🔄 Control Flow

### If/Else
```amharic
ከሆነ አድሜ >= 18 {
    ማተም "አዋቂ"
} አለበለዚያ {
    ማተም "ልጅ"
}
```

### While Loop
```amharic
አስተዋውቅ ቁጥር = 1
ሳለ ቁጥር <= 5 {
    ማተም ቁጥር
    ቁጥር = ቁጥር + 1
}
```

### For Loop
```amharic
ለ ቁጥር በ ወሰን(1, 6) {
    ማተም ቁጥር
}
```

## 🔧 Functions

### Definition
```amharic
ዘዴ ማተም_ስም(ስም) {
    ማተም "ስም:", ስም
}
```

### Call
```amharic
ማተም_ስም("አሊ")
```

### Return
```amharic
ዘዴ የማባዛት(ሀ, ለ) {
    መለስ ሀ * ለ
}
```

## 🏗️ Classes & Objects

### Class Definition
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
```

### Object Creation
```amharic
አስተዋውቅ ሰው_1 = አዲስ ሰው("አሊ", 25)
```

### Method Call
```amharic
ሰው_1.ማተም_መረጃ()
```

### Property Access
```amharic
ማተም ሰው_1.ስም
```

## 🛡️ Error Handling

### Try/Catch/Finally
```amharic
ሞክር {
    አስተዋውቅ ቁጥር = 10 / 0
} ያዝ ስህተት {
    ማተም "ስህተት ተፈጥሯል:", ስህተት
} በመጨረሻ {
    ማተም "አልተለወጠም"
}
```

### Throw Exception
```amharic
አስተላልፍ "ስህተት ተፈጥሯል!"
```

## 📁 File Operations

### Write File
```amharic
ጻፍ "test.txt" "Hello World"
```

### Read File
```amharic
አስተዋውቅ ይዘት = አንብብ "test.txt"
```

### Append File
```amharic
ጨምር "test.txt" "New content"
```

### Check File Exists
```amharic
ከሆነ አለ "test.txt" {
    ማተም "ፋይል አለ"
}
```

### Delete File
```amharic
ሰርዝ "test.txt"
```

### List Directory
```amharic
አስተዋውቅ ፋይሎች = ዝርዝር "."
```

### Create Directory
```amharic
ፍጠር "new_folder"
```

## 🔧 Built-in Functions

### Type Functions
```amharic
ዓይነት(ተለዋዋጭ)  # Get type
ቁጥር(ጽሑፍ)  # Convert to number
ጽሑፍ(ቁጥር)  # Convert to string
```

### Math Functions
```amharic
ከፍተኛ(1, 2, 3)  # Maximum
ዠቅተኛ(1, 2, 3)  # Minimum
```

### String Functions
```amharic
ርዝመት(ጽሑፍ)  # Length
ክፍል(ጽሑፍ, ክፍል)  # Split
አገናኝ(ጽሑፍ1, ጽሑፍ2)  # Join
ወደላይ(ጽሑፍ)  # Uppercase
ወደታች(ጽሑፍ)  # Lowercase
ተክ(ጽሑፍ, አሮጌ, አዲስ)  # Replace
```

### Range Function
```amharic
ወሰን(1, 10)  # Range from 1 to 10
```

## 📊 Data Structures

### List Operations
```amharic
አስተዋውቅ ዝርዝር = [1, 2, 3]
ማተም ዝርዝር[0]  # Access element
ዝርዝር[0] = 10  # Modify element
```

### Dictionary Operations
```amharic
አስተዋውቅ ንብብ = {"ስም": "አሊ"}
ማተም ንብብ["ስም"]  # Access value
ንብብ["አድሜ"] = 25  # Add/modify value
```

### Dictionary Methods
```amharic
ጨምር_ወደ ንብብ "አድሜ" 25
ሰርዝ_ከ ንብብ "አድሜ"
አለ_በ ንብብ "ስም"  # Check if key exists
```

## 🎯 Best Practices

1. **Use meaningful variable names in Amharic**
2. **Comment your code with Amharic explanations**
3. **Handle errors gracefully with try/catch**
4. **Use classes for complex data structures**
5. **Follow consistent indentation**

## 🚀 Advanced Features

### Inheritance (Coming Soon)
```amharic
ክፍል ተማሪ ተወላጅ ሰው {
    # Student class inherits from Person
}
```

### Modules (Coming Soon)
```amharic
አመጣ "math_module"
```

---

**Happy coding in Amharic! 🇪🇹**
