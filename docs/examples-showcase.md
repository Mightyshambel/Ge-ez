# Ge-ez Examples Showcase

Welcome to the Ge-ez examples showcase! Here you'll find comprehensive examples demonstrating all the features of the Amharic programming language.

## 📚 Table of Contents

- [Basic Examples](#basic-examples)
- [Control Flow](#control-flow)
- [Functions](#functions)
- [Object-Oriented Programming](#object-oriented-programming)
- [File Operations](#file-operations)
- [Error Handling](#error-handling)
- [Data Structures](#data-structures)
- [Advanced Examples](#advanced-examples)

## 🚀 Basic Examples

### Hello World
```amharic
ማተም "ሰላም ዓለም!"
```

### Variables
```amharic
አስተዋውቅ ስም = "አሊ"
አስተዋውቅ አድሜ = 25
አስተዋውቅ አውታረመረብ = እውነት

ማተም "ስም:", ስም
ማተም "አድሜ:", አድሜ
ማተም "አውታረመረብ:", አውታረመረብ
```

### User Input
```amharic
አስተዋውቅ ስም = ግብአት("ስምዎን ያስገቡ: ")
ማተም "ሰላም", ስም
```

## 🔄 Control Flow

### If/Else Statements
```amharic
አስተዋውቅ አድሜ = 20

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

### Basic Function
```amharic
ዘዴ ማተም_ስም(ስም) {
    ማተም "ስም:", ስም
}

ማተም_ስም("አሊ")
```

### Function with Return
```amharic
ዘዴ የማባዛት(ሀ, ለ) {
    መለስ ሀ * ለ
}

አስተዋውቅ ውጤት = የማባዛት(5, 3)
ማተም "ውጤት:", ውጤት
```

### Recursive Function
```amharic
ዘዴ ፋቢኖቺ(ቁጥር) {
    ከሆነ ቁጥር <= 1 {
        መለስ ቁጥር
    } አለበለዚያ {
        መለስ ፋቢኖቺ(ቁጥር - 1) + ፋቢኖቺ(ቁጥር - 2)
    }
}

ለ ቁጥር በ ወሰን(1, 11) {
    ማተም ፋቢኖቺ(ቁጥር)
}
```

## 🏗️ Object-Oriented Programming

### Simple Class
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
    
    ዘዴ አድሜ_መጨመር(ራሱ) {
        ራሱ.አድሜ = ራሱ.አድሜ + 1
    }
}

# Create objects
አስተዋውቅ ሰው_1 = አዲስ ሰው("አሊ", 25)
አስተዋውቅ ሰው_2 = አዲስ ሰው("ብርሃን", 30)

# Use objects
ሰው_1.ማተም_መረጃ()
ሰው_2.ማተም_መረጃ()

ሰው_1.አድሜ_መጨመር()
ማተም "አዲስ አድሜ:", ሰው_1.አድሜ
```

### Calculator Class
```amharic
ክፍል ካልኩሌተር {
    ዘዴ መጀመሪያ(ራሱ) {
        ራሱ.ውጤት = 0
    }
    
    ዘዴ መጨመር(ራሱ, ቁጥር) {
        ራሱ.ውጤት = ራሱ.ውጤት + ቁጥር
        መለስ ራሱ.ውጤት
    }
    
    ዘዴ መቀነስ(ራሱ, ቁጥር) {
        ራሱ.ውጤት = ራሱ.ውጤት - ቁጥር
        መለስ ራሱ.ውጤት
    }
    
    ዘዴ ማባዛት(ራሱ, ቁጥር) {
        ራሱ.ውጤት = ራሱ.ውጤት * ቁጥር
        መለስ ራሱ.ውጤት
    }
    
    ዘዴ ማተም_ውጤት(ራሱ) {
        ማተም "ውጤት:", ራሱ.ውጤት
    }
}

አስተዋውቅ ካልኩ = አዲስ ካልኩሌተር()
ካልኩ.መጨመር(10)
ካልኩ.ማባዛት(2)
ካልኩ.መቀነስ(5)
ካልኩ.ማተም_ውጤት()
```

## 📁 File Operations

### File Writing and Reading
```amharic
# Write to file
ጻፍ "test.txt" "ሰላም ዓለም!"

# Read from file
አስተዋውቅ ይዘት = አንብብ "test.txt"
ማተም "የፋይል ይዘት:", ይዘት

# Append to file
ጨምር "test.txt" " አዲስ ይዘት"

# Check if file exists
ከሆነ አለ "test.txt" {
    ማተም "ፋይል አለ"
} አለበለዚያ {
    ማተም "ፋይል አልተገኘም"
}
```

### Directory Operations
```amharic
# Create directory
ፍጠር "test_folder"

# List files
አስተዋውቅ ፋይሎች = ዝርዝር "."
ለ ፋይል በ ፋይሎች {
    ማተም ፋይል
}
```

## 🛡️ Error Handling

### Basic Try/Catch
```amharic
ሞክር {
    አስተዋውቅ ቁጥር = 10 / 0
} ያዝ ስህተት {
    ማተም "ስህተት ተፈጥሯል:", ስህተት
}
```

### Try/Catch/Finally
```amharic
ሞክር {
    አስተዋውቅ ፋይል = አንብብ "nonexistent.txt"
    ማተም ፋይል
} ያዝ ስህተት {
    ማተም "ፋይል አልተገኘም:", ስህተት
} በመጨረሻ {
    ማተም "አልተለወጠም"
}
```

### Custom Error Throwing
```amharic
ዘዴ አድሜ_መፈተሽ(አድሜ) {
    ከሆነ አድሜ < 0 {
        አስተላልፍ "አድሜ አሉታዊ ሊሆን አይችልም"
    }
    ከሆነ አድሜ > 150 {
        አስተላልፍ "አድሜ በጣም ትልቅ ነው"
    }
    ማተም "አድሜ ተቀባይነት አለው:", አድሜ
}

ሞክር {
    አድሜ_መፈተሽ(-5)
} ያዝ ስህተት {
    ማተም "ስህተት:", ስህተት
}
```

## 📊 Data Structures

### Lists
```amharic
አስተዋውቅ ቁጥሮች = [1, 2, 3, 4, 5]
አስተዋውቅ ስሞች = ["አሊ", "ብርሃን", "ሰላም"]

# Access elements
ማተም ቁጥሮች[0]  # First element
ማተም ስሞች[2]  # Third element

# Modify elements
ቁጥሮች[0] = 10
ማተም ቁጥሮች[0]

# Iterate through list
ለ ቁጥር በ ቁጥሮች {
    ማተም ቁጥር
}
```

### Dictionaries
```amharic
አስተዋውቅ ሰው = {"ስም": "አሊ", "አድሜ": 25, "አውታረመረብ": እውነት}

# Access values
ማተም ሰው["ስም"]
ማተም ሰው["አድሜ"]

# Add new key-value pairs
ሰው["ከተማ"] = "አዲስ አበባ"

# Check if key exists
ከሆነ አለ_በ ሰው "ከተማ" {
    ማተም "ከተማ:", ሰው["ከተማ"]
}

# Dictionary operations
ጨምር_ወደ ሰው "ስራ" "ፕሮግራመር"
ሰርዝ_ከ ሰው "አውታረመረብ"
```

## 🎯 Advanced Examples

### Simple Calculator
```amharic
ዘዴ ካልኩሌት(ሀ, ለ, ስራ) {
    ከሆነ ስራ == "+" {
        መለስ ሀ + ለ
    } አለበለዚያ ከሆነ ስራ == "-" {
        መለስ ሀ - ለ
    } አለበለዚያ ከሆነ ስራ == "*" {
        መለስ ሀ * ለ
    } አለበለዚያ ከሆነ ስራ == "/" {
        ከሆነ ለ != 0 {
            መለስ ሀ / ለ
        } አለበለዚያ {
            አስተላልፍ "በዜሮ መከፋፈል አይቻልም"
        }
    } አለበለዚያ {
        አስተላልፍ "ያልታወቀ ስራ"
    }
}

ሞክር {
    አስተዋውቅ ውጤት = ካልኩሌት(10, 5, "+")
    ማተም "ውጤት:", ውጤት
} ያዝ ስህተት {
    ማተም "ስህተት:", ስህተት
}
```

### Number Guessing Game
```amharic
ዘዴ የቁጥር_ጨዋታ() {
    አስተዋውቅ የተሰወረ_ቁጥር = 42
    አስተዋውቅ ሙከራዎች = 0
    አስተዋውቅ አሸናፊ = ሐሰት
    
    ማተም "በ 1 እና 100 መካከል ያለ ቁጥር አስብ!"
    
    ሳለ አሸናፊ == ሐሰት {
        አስተዋውቅ ግምት = ቁጥር(ግብአት("ግምትዎን ያስገቡ: "))
        ሙከራዎች = ሙከራዎች + 1
        
        ከሆነ ግምት == የተሰወረ_ቁጥር {
            ማተም "አሸናፊ! በ", ሙከራዎች, "ሙከራዎች"
            አሸናፊ = እውነት
        } አለበለዚያ ከሆነ ግምት < የተሰወረ_ቁጥር {
            ማተም "በጣም ትንሽ!"
        } አለበለዚያ {
            ማተም "በጣም ትልቅ!"
        }
    }
}

የቁጥር_ጨዋታ()
```

### File Processing
```amharic
ዘዴ ፋይል_መስመሮች_መቁጠር(ፋይል_ስም) {
    አስተዋውቅ ይዘት = አንብብ ፋይል_ስም
    አስተዋውቅ መስመሮች = ክፍል(ይዘት, "\n")
    አስተዋውቅ ቁጥር = ርዝመት(መስመሮች)
    
    ማተም "ፋይል", ፋይል_ስም, "ውስጥ", ቁጥር, "መስመሮች አሉ"
    መለስ ቁጥር
}

# Create a test file
ጻፍ "test.txt" "መስመር 1\nመስመር 2\nመስመር 3"

# Count lines
ፋይል_መስመሮች_መቁጠር("test.txt")
```

## 🎨 Creative Examples

### ASCII Art Generator
```amharic
ዘዴ አስኪ_አርት_መፍጠር(ጽሑፍ) {
    አስተዋውቅ ርዝመት = ርዝመት(ጽሑፍ)
    
    # Top border
    ማተም "┌" + አገናኝ(ርዝመት + 2, "─") + "┐"
    
    # Text line
    ማተም "│ " + ጽሑፍ + " │"
    
    # Bottom border
    ማተም "└" + አገናኝ(ርዝግት + 2, "─") + "┘"
}

አስኪ_አርት_መፍጠር("ሰላም ዓለም!")
```

### Simple Database Simulation
```amharic
ክፍል ዳታቤዝ {
    ዘዴ መጀመሪያ(ራሱ) {
        ራሱ.ውሂቦች = {}
    }
    
    ዘዴ መጨመር(ራሱ, ቁልፍ, ዋጋ) {
        ራሱ.ውሂቦች[ቁልፍ] = ዋጋ
        ማተም "ውሂብ ተጨመረ:", ቁልፍ, "=", ዋጋ
    }
    
    ዘዴ መፈለግ(ራሱ, ቁልፍ) {
        ከሆነ አለ_በ ራሱ.ውሂቦች ቁልፍ {
            መለስ ራሱ.ውሂቦች[ቁልፍ]
        } አለበለዚያ {
            መለስ "አልተገኘም"
        }
    }
    
    ዘዴ ማተም_ሁሉ(ራሱ) {
        ማተም "ዳታቤዝ ይዘት:"
        ለ ቁልፍ በ ራሱ.ውሂቦች {
            ማተም ቁልፍ, ":", ራሱ.ውሂቦች[ቁልፍ]
        }
    }
}

አስተዋውቅ ዳታቤዝ = አዲስ ዳታቤዝ()
ዳታቤዝ.መጨመር("ስም", "አሊ")
ዳታቤዝ.መጨመር("አድሜ", 25)
ዳታቤዝ.መጨመር("ከተማ", "አዲስ አበባ")

ማተም "የተፈለገ ውሂብ:", ዳታቤዝ.መፈለግ("ስም")
ዳታቤዝ.ማተም_ሁሉ()
```

---

**These examples demonstrate the power and flexibility of Ge-ez! Try running them and experiment with your own Amharic programs. 🇪🇹**
