// @(#)root/meta:$Id$
// Author: Philippe Canal 08/05/2002

/*************************************************************************
 * Copyright (C) 1995-2002, Rene Brun, Fons Rademakers and al.           *
 * All rights reserved.                                                  *
 *                                                                       *
 * For the licensing terms see $ROOTSYS/LICENSE.                         *
 * For the list of contributors see $ROOTSYS/README/CREDITS.             *
 *************************************************************************/

#include "TROOT.h"
#include "TClass.h"
#include "TClassEdit.h"
#include "TVirtualStreamerInfo.h"
#include "TStreamer.h"
#include "TVirtualIsAProxy.h"
#include "TVirtualCollectionProxy.h"
#include "TCollectionProxyInfo.h"
#include "TError.h"
#include "TVirtualMutex.h"
#include "TInterpreter.h"
#include "TClassTable.h"


namespace CppyyLegacy {

namespace Internal {

   std::string GetDemangledTypeName(const std::type_info &t)
   {
      int status = 0;
      char *name = TClassEdit::DemangleName(t.name(), status);

      if (!name || status != 0)
         return "";

      std::string ret;
      TClassEdit::GetNormalizedName(ret, name);
      free(name);
      return ret;
   }

   const TInitBehavior *DefineBehavior(void * /*parent_type*/,
                                       void * /*actual_type*/)
   {

      // This function loads the default behavior for the
      // loading of classes.

      static TDefaultInitBehavior theDefault;
      return &theDefault;
   }

   void TCDGIILIBase::SetInstance(CppyyLegacy::TGenericClassInfo& R__instance,
                                  NewFunc_t New, NewArrFunc_t NewArray,
                                  DelFunc_t Delete, DelArrFunc_t DeleteArray,
                                  DesFunc_t Destruct) {
         R__LOCKGUARD(gROOTMutex);
         R__instance.SetNew(New);
         R__instance.SetNewArray(NewArray);
         R__instance.SetDelete(Delete);
         R__instance.SetDeleteArray(DeleteArray);
         R__instance.SetDestructor(Destruct);
         R__instance.SetImplFile("", -1);
   }

   void TCDGIILIBase::SetName(const std::string& name,
                              std::string& nameMember) {
      R__LOCKGUARD(gInterpreterMutex);
      if (nameMember.empty()) {
         TClassEdit::GetNormalizedName(nameMember, name);
      }
   }

   void TCDGIILIBase::SetfgIsA(atomic_TClass_ptr& isA, TClass*(*dictfun)()) {
      if (!isA.load()) {
         R__LOCKGUARD(gInterpreterMutex);
         dictfun();
      }
   }
} // Internal


   TGenericClassInfo::TGenericClassInfo(const char *fullClassname,
                                        const char *declFileName, Int_t declFileLine,
                                        const std::type_info &info, const Internal::TInitBehavior  *action,
                                        DictFuncPtr_t dictionary,
                                        TVirtualIsAProxy *isa, Int_t pragmabits, Int_t sizof)
      : fAction(action), fClass(0), fClassName(fullClassname),
        fDeclFileName(declFileName), fDeclFileLine(declFileLine),
        fDictionary(dictionary), fInfo(info),
        fImplFileName(0), fImplFileLine(0), fIsA(isa), fVersion(1),
        fNew(0),fNewArray(0),fDelete(0),fDeleteArray(0),fDestructor(0), fStreamer(0),
        fStreamerFunc(0), fConvStreamerFunc(0), fCollectionProxy(0), fSizeof(sizof), fPragmaBits(pragmabits),
        fCollectionProxyInfo(0), fCollectionStreamerInfo(0)
   {
      // Constructor.

      Init(pragmabits);
   }

   TGenericClassInfo::TGenericClassInfo(const char *fullClassname, Int_t version,
                                        const char *declFileName, Int_t declFileLine,
                                        const std::type_info &info, const Internal::TInitBehavior  *action,
                                        DictFuncPtr_t dictionary,
                                        TVirtualIsAProxy *isa, Int_t pragmabits, Int_t sizof)
      : fAction(action), fClass(0), fClassName(fullClassname),
        fDeclFileName(declFileName), fDeclFileLine(declFileLine),
        fDictionary(dictionary), fInfo(info),
        fImplFileName(0), fImplFileLine(0), fIsA(isa), fVersion(version),
        fNew(0),fNewArray(0),fDelete(0),fDeleteArray(0),fDestructor(0), fStreamer(0),
        fStreamerFunc(0), fConvStreamerFunc(0), fCollectionProxy(0), fSizeof(sizof), fPragmaBits(pragmabits),
        fCollectionProxyInfo(0), fCollectionStreamerInfo(0)

   {
      // Constructor with version number and no showmembers.

      Init(pragmabits);
   }

   class TForNamespace {}; // Dummy class to give a typeid to namespace (See also TClassTable.cc)

   TGenericClassInfo::TGenericClassInfo(const char *fullClassname, Int_t version,
                                        const char *declFileName, Int_t declFileLine,
                                        const Internal::TInitBehavior  *action,
                                        DictFuncPtr_t dictionary, Int_t pragmabits)
      : fAction(action), fClass(0), fClassName(fullClassname),
        fDeclFileName(declFileName), fDeclFileLine(declFileLine),
        fDictionary(dictionary), fInfo(typeid(TForNamespace)),
        fImplFileName(0), fImplFileLine(0), fIsA(0), fVersion(version),
        fNew(0),fNewArray(0),fDelete(0),fDeleteArray(0),fDestructor(0), fStreamer(0),
        fStreamerFunc(0), fConvStreamerFunc(0), fCollectionProxy(0), fSizeof(0), fPragmaBits(pragmabits),
        fCollectionProxyInfo(0), fCollectionStreamerInfo(0)

   {
      // Constructor for namespace

      Init(pragmabits);
   }

   void TGenericClassInfo::Init(Int_t pragmabits)
   {
      // Initilization routine.

      //TVirtualStreamerInfo::Class_Version MUST be the same as TStreamerInfo::Class_Version
      if (fVersion==-2) fVersion = TVirtualStreamerInfo::Class_Version();
      if (!fAction) return;
      GetAction().Register(fClassName,
                           fVersion,
                           fInfo, // typeid(RootClass),
                           fDictionary,
                           pragmabits);
   }

   TGenericClassInfo::~TGenericClassInfo()
   {
      // Destructor.

      delete fCollectionProxyInfo;
      delete fCollectionStreamerInfo;
      delete fStreamer;
      if (!fClass) delete fIsA; // fIsA is adopted by the class if any.
      fIsA = 0;
      using CppyyLegacy::Internal::gROOTLocal;
      if (!gROOTLocal || !gROOTLocal->Initialized() || !gROOTLocal->GetListOfClasses()) return;
      if (fAction) GetAction().Unregister(GetClassName());
   }

   const Internal::TInitBehavior &TGenericClassInfo::GetAction() const
   {
      // Return the creator action.

      return *fAction;
   }

   TClass *TGenericClassInfo::GetClass()
   {
      // Generate and return the TClass object.

      // First make sure that TROOT is initialized, do this before checking
      // for fClass.  If the request is for the TClass of TObject and TROOT
      // is not initialized, the TROOT creation (because of the ROOT pcm files)
      // will lead to its own request of the TClass for TObject and thus
      // upon returning, the TClass for TObject will have already been created
      // and fClass will have been set.
      if (!gROOT)
         ::CppyyLegacy::Fatal("TClass::TClass", "ROOT system not initialized");

      if (!fClass && fAction) {
         R__LOCKGUARD(gInterpreterMutex);
         // Check again, while we waited for the lock, something else might
         // have set fClass.
         if (fClass) return fClass;

         fClass = GetAction().CreateClass(GetClassName(),
                                          GetVersion(),
                                          GetInfo(),
                                          GetIsA(),
                                          GetDeclFileName(),
                                          GetImplFileName(),
                                          GetDeclFileLine(),
                                          GetImplFileLine());
         if (fPragmaBits & TClassTable::kHasCustomStreamerMember) {
            fClass->SetBit(TClass::kHasCustomStreamerMember);
         }
         fClass->SetNew(fNew);
         fClass->SetNewArray(fNewArray);
         fClass->SetDelete(fDelete);
         fClass->SetDeleteArray(fDeleteArray);
         fClass->SetDestructor(fDestructor);
         fClass->SetStreamerFunc(fStreamerFunc);
         fClass->SetConvStreamerFunc(fConvStreamerFunc);
         fClass->AdoptStreamer(fStreamer); fStreamer = 0;
         // If IsZombie is true, something went wrong and we will not be
         // able to properly copy the collection proxy
         if (!fClass->IsZombie()) {
            if (fCollectionProxy) fClass->CopyCollectionProxy(*fCollectionProxy);
            else if (fCollectionProxyInfo) {
               fClass->SetCollectionProxy(*fCollectionProxyInfo);
            }
         }
         fClass->SetClassSize(fSizeof);

      }
      return fClass;
   }

   const char *TGenericClassInfo::GetClassName() const
   {
      // Return the class name

      return fClassName;
   }


   Detail::TCollectionProxyInfo *TGenericClassInfo::GetCollectionProxyInfo() const
   {
      // Return the set of info we have for the CollectionProxy, if any

      return fCollectionProxyInfo;
   }

   Detail::TCollectionProxyInfo *TGenericClassInfo::GetCollectionStreamerInfo() const
   {
      // Return the set of info we have for the Collection Streamer, if any

      return fCollectionProxyInfo;
   }

   const std::type_info &TGenericClassInfo::GetInfo() const
   {
      // Return the typeinfo value

      return fInfo;
   }

   void TGenericClassInfo::SetFromTemplate()
   {
      // Import the information from the class template.

      TNamed *info = CppyyLegacy::RegisterClassTemplate(GetClassName(), 0, 0);
      if (info) SetImplFile(info->GetTitle(), info->GetUniqueID());
   }

   Int_t TGenericClassInfo::SetImplFile(const char *file, Int_t line)
   {
      // Set the name of the implementation file.

      fImplFileName = file;
      fImplFileLine = line;
      if (fClass) fClass->AddImplFile(file,line);
      return 0;
   }

   Int_t TGenericClassInfo::SetDeclFile(const char *file, Int_t line)
   {
      // Set the name of the declaration file.

      fDeclFileName = file;
      fDeclFileLine = line;
      if (fClass) fClass->SetDeclFile(file,line);
      return 0;
   }

   Short_t TGenericClassInfo::SetVersion(Short_t version)
   {
      // Set a class version number.

      CppyyLegacy::ResetClassVersion(fClass, GetClassName(),version);
      fVersion = version;
      return version;
   }

   void TGenericClassInfo::AdoptCollectionProxyInfo(TCollectionProxyInfo *info)
   {
      // Set the info for the CollectionProxy and take ownership of the object
      // being passed

      delete fCollectionProxyInfo;;
      fCollectionProxyInfo = info;
   }

   void TGenericClassInfo::AdoptCollectionStreamerInfo(TCollectionProxyInfo *info)
   {
      // Set the info for the Collection Streamer and take ownership of the object
      // being passed

      delete fCollectionStreamerInfo;
      fCollectionStreamerInfo = info;
   }

   Short_t TGenericClassInfo::AdoptStreamer(TClassStreamer *streamer)
   {
      // Set a Streamer object.  The streamer object is now 'owned'
      // by the TGenericClassInfo.

      delete fStreamer; fStreamer = 0;
      if (fClass) {
         fClass->AdoptStreamer(streamer);
      } else {
         fStreamer = streamer;
      }
      return 0;
   }

   Short_t TGenericClassInfo::AdoptCollectionProxy(TVirtualCollectionProxy *collProxy)
   {
      // Set the CollectProxy object.  The CollectionProxy object is now 'owned'
      // by the TGenericClassInfo.

      delete fCollectionProxy; fCollectionProxy = 0;
      fCollectionProxy = collProxy;
      if (fClass && fCollectionProxy && !fClass->IsZombie()) {
         fClass->CopyCollectionProxy(*fCollectionProxy);
      }
      return 0;
   }

   Short_t TGenericClassInfo::SetStreamer(ClassStreamerFunc_t streamer)
   {
      // Set a External Streamer function.

      delete fStreamer; fStreamer = 0;
      if (fClass) {
         fClass->AdoptStreamer(new TClassStreamer(streamer));
      } else {
         fStreamer = new TClassStreamer(streamer);
      }
      return 0;
   }

   void TGenericClassInfo::SetStreamerFunc(ClassStreamerFunc_t streamer)
   {
      // Set a wrapper around the Streamer member function.

      fStreamerFunc = streamer;
      if (fClass) fClass->SetStreamerFunc(streamer);
   }

   void TGenericClassInfo::SetConvStreamerFunc(ClassConvStreamerFunc_t streamer)
   {
      // Set a wrapper around the Streamer member function.

      fConvStreamerFunc = streamer;
      if (fClass) fClass->SetConvStreamerFunc(streamer);
   }

   const char *TGenericClassInfo::GetDeclFileName() const
   {
      // Get the name of the declaring header file.

      return fDeclFileName;
   }

   Int_t TGenericClassInfo::GetDeclFileLine() const
   {
      // Get the declaring line number.

      return fDeclFileLine;
   }

   const char *TGenericClassInfo::GetImplFileName()
   {
      // Get the implementation filename.

      if (!fImplFileName) SetFromTemplate();
      return fImplFileName;
   }

   Int_t TGenericClassInfo::GetImplFileLine()
   {
      // Get the ClassImp line number.

      if (!fImplFileLine) SetFromTemplate();
      return fImplFileLine;
   }

   Int_t TGenericClassInfo::GetVersion() const
   {
      // Return the class version number.

      return fVersion;
   }

   TClass *TGenericClassInfo::IsA(const void *obj)
   {
      // Return the actual type of the object.

      return (*GetIsA())(obj);
   }

   TVirtualIsAProxy* TGenericClassInfo::GetIsA() const
   {
      // Return the IsA proxy.

      return fIsA;
   }

   void TGenericClassInfo::SetNew(NewFunc_t newFunc)
   {
      // Install a new wrapper around 'new'.

      fNew = newFunc;
      if (fClass) fClass->SetNew(fNew);
   }

   void TGenericClassInfo::SetNewArray(NewArrFunc_t newArrayFunc)
   {
      // Install a new wrapper around 'new []'.

      fNewArray = newArrayFunc;
      if (fClass) fClass->SetNewArray(fNewArray);
   }

   void TGenericClassInfo::SetDelete(DelFunc_t deleteFunc)
   {
      // Install a new wrapper around 'delete'.

      fDelete = deleteFunc;
      if (fClass) fClass->SetDelete(fDelete);
   }

   void TGenericClassInfo::SetDeleteArray(DelArrFunc_t deleteArrayFunc)
   {
      // Install a new wrapper around 'delete []'.

      fDeleteArray = deleteArrayFunc;
      if (fClass) fClass->SetDeleteArray(fDeleteArray);
   }

   void TGenericClassInfo::SetDestructor(DesFunc_t destructorFunc)
   {
      // Install a new wrapper around the destructor.

      fDestructor = destructorFunc;
      if (fClass) fClass->SetDestructor(fDestructor);
   }

   NewFunc_t TGenericClassInfo::GetNew() const
   {
      // Get the wrapper around 'new'.

      return fNew;
   }

   NewArrFunc_t TGenericClassInfo::GetNewArray() const
   {
      // Get the wrapper around 'new []'.

      return fNewArray;
   }

   DelFunc_t TGenericClassInfo::GetDelete() const
   {
      // Get the wrapper around 'delete'.

      return fDelete;
   }

   DelArrFunc_t TGenericClassInfo::GetDeleteArray() const
   {
      // Get the wrapper around 'delete []'.

      return fDeleteArray;
   }

   DesFunc_t TGenericClassInfo::GetDestructor() const
   {
      // Get the wrapper around the destructor.

      return fDestructor;
   }

} // namespace CppyyLegacy
