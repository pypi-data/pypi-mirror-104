// @(#)root/cont:$Id$
// Author: Rene Brun   06/03/95

/*************************************************************************
 * Copyright (C) 1995-2000, Rene Brun and Fons Rademakers.               *
 * All rights reserved.                                                  *
 *                                                                       *
 * For the licensing terms see $ROOTSYS/LICENSE.                         *
 * For the list of contributors see $ROOTSYS/README/CREDITS.             *
 *************************************************************************/

#ifndef ROOT_TArrayC
#define ROOT_TArrayC


//////////////////////////////////////////////////////////////////////////
//                                                                      //
// TArrayC                                                              //
//                                                                      //
// Array of chars or bytes (8 bits per element).                        //
//                                                                      //
//////////////////////////////////////////////////////////////////////////

#include "TArray.h"


namespace CppyyLegacy {

class TArrayC : public TArray {

public:
   Char_t    *fArray;       //[fN] Array of fN chars

   TArrayC();
   TArrayC(Int_t n);
   TArrayC(Int_t n, const Char_t *array);
   TArrayC(const TArrayC &array);
   TArrayC    &operator=(const TArrayC &rhs);
   virtual    ~TArrayC();

   void          Adopt(Int_t n, Char_t *array);
   void          AddAt(Char_t c, Int_t i);
   Char_t        At(Int_t i) const ;
   void          Copy(TArrayC &array) const {array.Set(fN,fArray);}
   const Char_t *GetArray() const { return fArray; }
   Char_t       *GetArray() { return fArray; }
   Double_t      GetAt(Int_t i) const { return At(i); }
   Stat_t        GetSum() const {Stat_t sum=0; for (Int_t i=0;i<fN;i++) sum+=fArray[i]; return sum;}
   void          Reset(Char_t val=0)  {memset(fArray,val,fN*sizeof(Char_t));}
   void          Set(Int_t n);
   void          Set(Int_t n, const Char_t *array);
   void          SetAt(Double_t v, Int_t i) { AddAt((Char_t)v, i); }
   Char_t       &operator[](Int_t i);
   Char_t        operator[](Int_t i) const;

   ClassDef(TArrayC,1)  //Array of chars
};

} // namespace CppyyLegacy

#if defined R__TEMPLATE_OVERLOAD_BUG
template <>
#endif
inline CppyyLegacy::TBuffer &operator>>(CppyyLegacy::TBuffer &buf, CppyyLegacy::TArrayC *&obj)
{
   // Read TArrayC object from buffer.

   obj = (CppyyLegacy::TArrayC *) CppyyLegacy::TArray::ReadArray(buf, CppyyLegacy::TArrayC::Class());
   return buf;
}

#if defined R__TEMPLATE_OVERLOAD_BUG
template <>
#endif
inline CppyyLegacy::TBuffer &operator<<(CppyyLegacy::TBuffer &buf, const CppyyLegacy::TArrayC *obj)
{
   // Write a TArrayC object into buffer
   return buf << (const CppyyLegacy::TArray*)obj;
}

namespace CppyyLegacy {

inline Char_t TArrayC::At(Int_t i) const
{
   if (!BoundsOk("TArrayC::At", i)) return 0;
   return fArray[i];
}

inline Char_t &TArrayC::operator[](Int_t i)
{
   if (!BoundsOk("TArrayC::operator[]", i))
      i = 0;
   return fArray[i];
}

inline Char_t TArrayC::operator[](Int_t i) const
{
   if (!BoundsOk("TArrayC::operator[]", i)) return 0;
   return fArray[i];
}

} // namespace CppyyLegacy

#endif
