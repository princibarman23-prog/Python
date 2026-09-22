n=int(input("Enter the number of elements:"))
st=[]
for i in range(n):
    x=int(input("Enter the elements:"))
    st.append(x)
y=st.reverse()
print("Stack of elements is:",st)