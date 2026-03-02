cpp
template <class T> // 'class T' is a type parameter. 'typename T' is also valid and preferred.
class ClassName {
// Class body using type T
T memberVariable;
public:
T getValue() { return memberVariable; }
void setValue(T value) { memberVariable = value; }
};
