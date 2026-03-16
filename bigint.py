class BigInt:
    def __init__(s,val=0):
        if isinstance(val,str): s.neg=val[0]=="-";s.digits=list(map(int,reversed(val.lstrip("-") or"0")))
        elif isinstance(val,int): s.neg=val<0;s.digits=list(map(int,reversed(str(abs(val))))) if val else[0]
        else: s.neg=val.neg;s.digits=list(val.digits)
    def __repr__(s):
        r="".join(map(str,reversed(s.digits))).lstrip("0") or"0"
        return("-" if s.neg and r!="0" else"")+r
    def _cmp(s,o):
        a,b=s.digits,o.digits
        if len(a)!=len(b): return 1 if len(a)>len(b) else -1
        for i in range(len(a)-1,-1,-1):
            if a[i]!=b[i]: return 1 if a[i]>b[i] else -1
        return 0
    def _add_abs(s,o):
        r=[];carry=0;n=max(len(s.digits),len(o.digits))
        for i in range(n):
            t=(s.digits[i] if i<len(s.digits) else 0)+(o.digits[i] if i<len(o.digits) else 0)+carry
            r.append(t%10);carry=t//10
        if carry: r.append(carry)
        return r
    def _sub_abs(s,o):
        r=[];borrow=0
        for i in range(len(s.digits)):
            t=s.digits[i]-(o.digits[i] if i<len(o.digits) else 0)-borrow
            if t<0: t+=10;borrow=1
            else: borrow=0
            r.append(t)
        while len(r)>1 and r[-1]==0: r.pop()
        return r
    def __add__(s,o):
        o=BigInt(o) if isinstance(o,int) else o;res=BigInt()
        if s.neg==o.neg: res.digits=s._add_abs(o);res.neg=s.neg
        else:
            if s._cmp(o)>=0: res.digits=s._sub_abs(o);res.neg=s.neg
            else: res.digits=o._sub_abs(s);res.neg=o.neg
        return res
    def __mul__(s,o):
        o=BigInt(o) if isinstance(o,int) else o;r=[0]*(len(s.digits)+len(o.digits))
        for i,a in enumerate(s.digits):
            for j,b in enumerate(o.digits): r[i+j]+=a*b
        for i in range(len(r)-1):
            r[i+1]+=r[i]//10;r[i]%=10
        while len(r)>1 and r[-1]==0: r.pop()
        res=BigInt();res.digits=r;res.neg=s.neg!=o.neg;return res
    def factorial(n):
        r=BigInt(1)
        for i in range(2,n+1): r=r*BigInt(i)
        return r
def demo():
    a=BigInt("123456789012345678901234567890");b=BigInt("987654321098765432109876543210")
    print(f"a+b = {a+b}");print(f"a*b = {a*b}");print(f"50! = {BigInt.factorial(50)}")
if __name__=="__main__": demo()
